#!/usr/bin/env bash
if ! which dialog &>/dev/null; then
    echo "Error: dialog command is required but not installed" >&2
    echo "       see https://command-not-found.com/dialog" >&2
    exit 1
fi

DIALOG_CANCEL=1
DIALOG_ESC=255

trap_ignore() {
    true
}
trap_exit() {
    clear
    exit 0
}
trap trap_exit INT

develtio() {
    trap trap_ignore INT
    make -C "${RUNNER_DIR}" "$@"
    trap trap_exit INT
}
develtio_dialog() {
    TITLE="$1"
    shift
    develtio "$@" 2>&1 | \
        dialog \
            --backtitle "Develtio Runner | ${TITLE}" \
            --no-collapse \
            --programbox 18 90
}
develtio_console() {
    clear
    develtio "$@" 2>&1
    echo
    read -p "Press Enter to continue"
}
develtio_status() {
    if ! make -s -C "${RUNNER_DIR}" debug-docker-compose CMD=ps 2>/dev/null | grep "_app_" | grep -q "Up"; then
        echo down
    else
        echo up
    fi
}

while true; do
    exec 3>&1
    selection=$(dialog \
        --backtitle "Develtio Runner | version=${RUNNER_VERSION}, dir=${RUNNER_DIR}" \
        --title "${APP} | dir=${APP_DIR}, env=${ENV}, status=$(develtio_status)" \
        --cancel-label "Exit" \
        --ok-label "OK" \
        --hline "" \
        --default-item "${selection:-}" \
        --menu "" 16 0 16 \
        "Build" "Build all application Docker images" \
        "Build Clean" "Build all application Docker images from scratch" \
        "History" "View application Docker image history" \
        "Start" "Start or restart all services" \
        "Stop" "Stop the application stack" \
        "Down" "Stop and cleanup the application stack" \
        "Exec" "Execute a command in the application container" \
        "Logs" "Stream all the services logs" \
        "Status" "View the status of all services" \
        "Config" "View combined docker-compose.yml of the application stack" \
        "Debug" "Show debug information" \
        "Debug Share" "Share debug information on a publicly available server" \
        "Debug Files" "List files loaded and used in this project" \
        "Debug Environment" "View all variables from a combined env file" \
        "Debug CLI - Network" "Enter debugging interface with shared network stack" \
        "Debug CLI - PID" "Enter debugging interface with shared PID stack" \
        "Debug CLI - Storage" "Enter debugging interface with shared storage" \
        "Remote Web" "Run a public web tunnel for the application" \
        "Remote Terminal" "Run a remote debugging session available publicly" \
        "Remote Status" "View the status of all containers related to remote services" \
        "Remote Logs" "View live terminal session including all commands executed" \
        "Remote Stop" "Stop all containers related to remote services" \
        2>&1 1>&3)
    exit_status=$?
    case $exit_status in
        $DIALOG_CANCEL)
            clear
            exit 0
            ;;
        $DIALOG_ESC)
            clear
            exit
            ;;
    esac
    case $selection in
        0)
            clear
            exit 0
            ;;
        Start|Stop|Down)
            develtio_dialog "$selection" "${selection,,}"
            ;;
        Build|Debug|Config|History)
            develtio_console "${selection,,}"
            ;;
        "Build Clean")
            develtio_console build-clean
            ;;
        Exec)
            RESULT=$(dialog --inputbox "Command:" 10 70 "bash" 2>&1 1>&3)
            exit_status=$?
            if [[ "0" != "$exit_status" ]]; then
                continue
            fi
            clear
            develtio_console exec CMD="$RESULT"
            ;;
        Status)
            develtio_dialog "$selection" ps
            ;;
        Logs)
            clear
            develtio logs
            ;;
        "Debug Share")
            develtio_console debug-share
            ;;
        "Debug Environment")
            develtio_console debug-env-file
            ;;
        "Debug CLI - Network")
            clear
            develtio net-cli
            ;;
        "Debug CLI - PID")
            clear
            develtio pid-cli
            ;;
        "Debug CLI - Storage")
            clear
            develtio storage-cli
            ;;
        "Debug Files")
            develtio_console debug-list-files
            ;;
        "Remote Web")
            develtio_console remote-web
            ;;
        "Remote Terminal")
            develtio_console remote-terminal
            ;;
        "Remote Status")
            develtio_dialog "$selection" remote-ps
            ;;
        "Remote Logs")
            clear
            develtio remote-logs
            ;;
        "Remote Stop")
            develtio_dialog "$selection" remote-stop
            ;;
    esac
    exec 3>&-
done