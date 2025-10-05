@echo off
REM SPSS Prep Tool - Windows Launcher
REM This batch file checks Python and launches the app

title SPSS Prep Tool

echo ============================================================
echo   SPSS Prep Tool - Windows Launcher
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH!
    echo.
    echo Please install Python 3.10 or higher from:
    echo https://www.python.org/downloads/
    echo.
    echo Make sure to check "Add Python to PATH" during installation!
    echo.
    pause
    exit /b 1
)

echo [INFO] Python detected
python --version
echo.

REM Run the launcher
echo [INFO] Starting launcher...
echo.
python launcher.py

REM If launcher exits, pause to show any error messages
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Launcher exited with error code %errorlevel%
    pause
)

