@echo off
SET SCRIPT_DIR=%~dp0
cd /d %SCRIPT_DIR%
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
deactivate
echo Virtual environment setup is complete and requirements are installed.
pause