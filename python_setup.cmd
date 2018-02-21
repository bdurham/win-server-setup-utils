@echo off
REM python_setup.cmd
REM Install Python for all users in \udp\python; copy helper scripts to C:\Windows
REM Options described at https://docs.python.org/3/using/windows.html
..\downloads\python-3.6.4-amd64.exe  /quiet  InstallAllUsers=1  DefaultAllUsersTargetDir=c:\udp\python  PrependPath=1 
copy /Y idle.cmd    c:\windows > nul
copy /Y pip.cmd     c:\windows > nul
copy /Y python.cmd  c:\windows > nul
copy /Y pythonw.cmd c:\windows > nul
