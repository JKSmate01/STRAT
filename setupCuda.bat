@echo off
SET SCRIPT_DIR=%~dp0
cd /d %SCRIPT_DIR%
python -m venv venv
call venv\Scripts\activate
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
deactivate
pause