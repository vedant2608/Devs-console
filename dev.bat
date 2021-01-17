@echo off
cls
echo Welcome to the DEV assistant. This can be used in Command line  mode.

echo "  ____    U _____ u    __     __   ";
echo " |  _\ \  \| ___\ |/   \ \   /\ /u  ";
echo "/| | | |   |  _|\       \ \ / //   ";
echo "U| |_| |\  | |___       /\ V /_,-. ";
echo " |____/ u  |_____|     U  \_/-(_/  ";
echo "  |||_     <<   >>       //        ";
echo " (__)_)   (__) (__)     (__)       ";

pause
cls
if not exist intro_repeat.exe python dev_intro.py
echo hii> intro_repeat.exe
cls
echo    starting DEV's Console...
timeout /t 2 /nobreak > NUL
echo "  ____    U _____ u    __     __   ";
echo " |  _\ \  \| ___\ |/   \ \   /\ /u  ";
echo "/| | | |   |  _|\       \ \ / //   ";
echo "U| |_| |\  | |___       /\ V /_,-. ";
echo " |____/ u  |_____|     U  \_/-(_/  ";
echo "  |||_     <<   >>       //        ";
echo " (__)_)   (__) (__)     (__)       ";

echo   type help or Enter the commands as you want use assistant
assistant.bat