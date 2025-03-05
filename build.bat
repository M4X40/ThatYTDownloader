@echo off && cls
pip install pyinstaller && cls
pyinstaller --onefile main.py && cls
del main.spec && rmdir /s /q build
echo Build done! Find it in \dist\main.exe && pause