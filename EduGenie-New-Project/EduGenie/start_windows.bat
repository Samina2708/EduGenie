@echo off
set "PROJECT_DIR=%~dp0"
cd /d "%PROJECT_DIR%"
"%PROJECT_DIR%.venv\Scripts\python.exe" -m uvicorn main:app --reload
