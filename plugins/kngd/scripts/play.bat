@echo off
REM Double-click me (Windows) to play your game.
REM I start a tiny local server and open your browser — then just play.
REM Close this window to stop.
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
  py play.py
  goto :eof
)
where python >nul 2>nul
if %errorlevel%==0 (
  python play.py
  goto :eof
)
echo.
echo Python isn't installed. Get it from https://www.python.org/downloads/
echo During install, tick "Add Python to PATH", then double-click me again.
echo.
pause
