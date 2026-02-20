@echo off
set SKILL_DIR=%~dp0
python -m venv "%SKILL_DIR%.venv"
call "%SKILL_DIR%.venv\Scripts\activate.bat"
pip install -r "%SKILL_DIR%requirements.txt"
call "%SKILL_DIR%.venv\Scripts\crawl4ai-setup.exe