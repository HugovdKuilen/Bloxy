py setup.py build
mkdir build\exe.win32-3.7\deathanim
mkdir build\exe.win32-3.7\levelcompleteanim
mkdir build\exe.win32-3.7\titlescreen
xcopy /s deathanim build\exe.win32-3.7\deathanim
xcopy /s levelcompleteanim build\exe.win32-3.7\levelcompleteanim
xcopy /s titlescreen build\exe.win32-3.7\titlescreen
xcopy /s "loading\Loading screen.png" build\exe.win32-3.7
xcopy /s loading\settings.txt build\exe.win32-3.7
pause