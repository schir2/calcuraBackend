@echo off
set PACKAGE=%1
pip install %PACKAGE%
pip freeze | findstr %PACKAGE% >> requirements.txt