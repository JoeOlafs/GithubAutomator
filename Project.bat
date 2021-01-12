@echo off

set fn=%1
set flag=%2

if "%1" == "" (
	echo error
) else (
	if "%2"=="py" (
		python git.py %fn% %flag%
	)
	if "%2"=="java" (
		python git.py %fn% %flag%
		) else (
            if "%2"=="" (
                echo local not ready
            )
        )    
	)
