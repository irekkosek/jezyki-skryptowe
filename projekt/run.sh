#!/usr/bin/env bash
while true; do
    exec 3>&1
    selection=$(dialog \
        --backtitle "Projekt" \
        --title "Projekt" \
        --cancel-label "Exit" \
        --ok-label "OK" \
        --hline "" \
        --default-item "${selection:-}" \
        --menu "" 16 0 16 \
        "Exec" "Execute the algorithm" \
        "Backup" "Backup the algorithm's output" \
        "Authors" "See info about Author(s)" \
        "Exit" "Exit the program" \
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
        Exec)
            if [[ "0" != "$exit_status" ]]; then
                continue
            fi
            clear
            python3 projekt.py
            ;;
        Backup)
            mkdir -p backup/$(date +%Y-%m-%d_%H-%M-%S)/
            set -x
            cp -r output backup/$(date +%Y-%m-%d_%H-%M-%S)/output 3>>logs 2>>logs
            cp -r input backup/$(date +%Y-%m-%d_%H-%M-%S)/input 3>>logs 2>>logs
            mv *.html "backup/$(date +%Y-%m-%d_%H-%M-%S)/" 3>>logs 2>>logs
            set +x
            ;;
        Authors)
            dialog \
                --backtitle "Projekt" \
                --title "Authors" \
                --msgbox "Author: Ireneusz Kosek" 0 0
            ;;
        Exit)
            clear
            exit 0
            ;;
    esac
    exec 3>&-
done