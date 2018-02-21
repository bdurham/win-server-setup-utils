@echo off
REM python_verify.cmd 
REM Verifies Python setup

echo PYTHON:            
python_verify.py        
echo.                   
echo ASSOC:             
assoc | find /I "python"
echo.                   
echo FTYPE:             
ftype | find /I "python"
