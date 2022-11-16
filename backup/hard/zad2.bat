@echo off
set /p file=Podaj plik: 
for %%F in (*.txt) do (
fc /b %%F %file% > nul
if errorlevel 1 (
    echo %%F >> inne.txt
) else (
    echo %%F >> identyczne.txt
)
)
sort inne.txt
sort identyczne.txt
pause