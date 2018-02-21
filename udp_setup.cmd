@echo off
REM udp_setup.cmd
REM Setup udp developer runtime environment

REM Create initial folders
md c:\udp            2> nul
md c:\udp\downloads  2> nul
md c:\udp\sandbox    2> nul

REM Download setup executables for git and python
REM Update file versions as new versions are released
echo Downloading git setup ...
powershell iwr -outf c:\udp\downloads\git-setup.exe     https://github.com/git-for-windows/git/releases/download/v2.16.1.windows.4/Git-2.16.1.4-64-bit.exe   
echo Downloading python setup ...
powershell iwr -outf c:\udp\downloads\python-setup.exe  https://www.python.org/ftp/python/3.6.4/python-3.6.4-amd64.exe

REM Move to sandbox folder to run setup and verification scripts
c:
cd c:\udp\sandbox
echo Continue with git, python, awscli setups



