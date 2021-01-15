@echo off

set fn=%1
set flag=%2

if "%1"=="" (
	echo error
) else (
    if "%2"=="" (
        echo local not ready
    ) else (
        python git_copy.py %fn% %flag%
    )
)