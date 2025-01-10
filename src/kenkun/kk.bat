@echo off
set pythonpath=%pythonpath%;src
call .venv\Scripts\activate.bat
python -m kenkun %*
