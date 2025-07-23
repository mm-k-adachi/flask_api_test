@echo off
setlocal

set current_dir=%~dp0
set current_dir=%current_dir:~0,-1%
set current_dir_slash=%current_dir:\=/%

echo %current_dir_slash%
git config --global --add safe.directory %current_dir_slash%
