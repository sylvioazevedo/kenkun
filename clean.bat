@echo off
call uv pip uninstall kenkun
call uv cache clean kenkun
call rmdir /S /Q build dist