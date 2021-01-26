@echo on

set fn=%1
set flag=%2
Set loc=%3

cd Progs
cd GithubAutomator

if "%1"=="" (
	echo error
) else (
    if "%2"=="" (
        echo error
    ) else (
        if "%2"=="flutter" (
            python gitFlutter.py %fn% %flag%
        ) else (
            if "%3" == "local" (
                python local.py %fn% %flag%
            ) else (
                python git.py %fn% %flag%
            )
        )
    )
)

cd ..
cd ..
