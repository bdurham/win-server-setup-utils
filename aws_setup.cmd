@echo off
REM aws_setup.cmd 
REM Install/upgrade AWS CLI; also installs/upgrades AWS Boto3 API
cmd /c pip install --upgrade awscli
copy /Y aws.cmd c:\windows > nul


