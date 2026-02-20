@REM This tool check if matlab is available and run a matlab command.
@REM Usage with commands: run_matlab_command.bat "matlab command"
@REM Usage with files: run_matlab_command.bat "matlab filename (without extension)"

@REM Check if matlab is available
where matlab >nul 2>&1
if %errorlevel% neq 0 (
    echo MATLAB is not available
    exit /b 1
)

@REM Run the matlab command
matlab -batch "%1"