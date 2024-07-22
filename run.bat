@echo off
SET SCRIPT_DIR=%~dp0
cd /d %SCRIPT_DIR%
call venv\Scripts\activate
api.py
pause