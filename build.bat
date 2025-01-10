@echo off
call uv run -m build

rem copy dist files to deploy directory
set DEPLOY_DIR=C:\Users\sazevedo\Documents\repo
call copy /Y dist\* %DEPLOY_DIR%\kenkun



