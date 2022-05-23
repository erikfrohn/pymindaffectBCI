<<<<<<< HEAD
cd %~dp0
=======
setlocal enabledelayedexpansion
set batdir=%~dp0
cd %batdir%
cd ..\mindaffectBCI\hub

>>>>>>> a548ede18b5df0b53d3ccd030994f9147272f202
java -cp UtopiaServer.jar nl.ma.utopiaserver.UtopiaClient selection
