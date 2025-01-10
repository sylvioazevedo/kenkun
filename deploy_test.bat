@echo off

rem Only for a first time
uv run twine upload --repository testpypi dist/* --verbose
