setlocal ENABLEDELAYEDEXPANSION
FOR %%G IN (*.txt) DO (
    for /F "tokens=*" %%A in (%%G) do (
        SET Quoted=%%A

        FOR /F "delims=" %%I IN (!Quoted!) DO SET Unquoted=%%I

        ECHO !Quoted!
        ECHO !Unquoted! >> %%G_unquoted.txt
    )
    MOVE /y %%G_unquoted.txt %%G
)
pause