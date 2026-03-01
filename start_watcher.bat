@echo off
cd /d "%USERPROFILE%\Desktop\AI_Employee_Vault"
echo Starting AI Employee Watcher...
python watcher.py
if %ERRORLEVEL% == 9009 (
    echo.
    echo ERROR: Python was not found. Please install Python and make sure it is added to your PATH.
    echo Download Python at: https://www.python.org/downloads/
)
pause
