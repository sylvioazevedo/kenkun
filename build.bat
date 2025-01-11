@echo off
rem delete dist directory
call rmdir /S /Q dist

call uv run -m build

rem copy dist files to deploy directory
set DEPLOY_DIR=C:\Users\sazevedo\Documents\repo
call copy /Y dist\* %DEPLOY_DIR%\kenkun



