@echo off
:: Check if Python is installed
python --version >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python 3.7 or later and try again.
    pause
    exit /b
)

:: Ensure pip is installed
python -m pip --version >nul 2>nul
if %errorlevel% neq 0 (
    echo Pip is not installed. Installing pip...
    python -m ensurepip --upgrade
)

:: Upgrade pip to avoid issues
echo Upgrading pip...
python -m pip install --upgrade pip

:: Install dependencies directly
echo Installing dependencies...
python -m pip install altgraph==0.17.4 auto-py-to-exe==2.45.1 bottle==0.13.2 bottle-websocket==0.2.9 certifi==2024.12.14 cffi==1.17.1 charset-normalizer==3.4.1 colorama==0.4.6 Eel==0.18.1 future==1.0.0 gevent==24.11.1 gevent-websocket==0.10.1 greenlet==3.1.1 idna==3.10 keyboard==0.13.5 MouseInfo==0.1.3 numpy==2.2.1 opencv-python==4.10.0.84 opencv-python-headless==4.10.0.84 pefile==2023.2.7 pillow==11.1.0 pip-chill==1.0.3 pyarmor==9.0.7 pyarmor.cli.core==7.6.2 PyAutoGUI==0.9.54 pycparser==2.22 PyGetWindow==0.0.9 pyinstaller-hooks-contrib==2024.11 PyMsgBox==1.0.9 pyparsing==3.2.1 pyperclip==1.9.0 PyRect==0.2.0 PyScreeze==1.0.1 pytweening==1.2.0 pywin32-ctypes==0.2.3 requests==2.32.3 typing_extensions==4.12.2 zope.event==5.0 zope.interface==7.2 --no-warn-script-location

:: Run the executable
echo Running your application...
start "" main.exe

pause
