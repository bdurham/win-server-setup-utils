@echo off
REM python_verify.cmd - verifies Python setup

echo PYTHON:              > python_verify.txt
python_verify.py         >> python_verify.txt
echo.                    >> python_verify.txt
echo ASSOC:              >> python_verify.txt
assoc | find /I "python" >> python_verify.txt
echo.                    >> python_verify.txt
echo FTYPE:              >> python_verify.txt
ftype | find /I "python" >> python_verify.txt
notepad python_verify.txt
