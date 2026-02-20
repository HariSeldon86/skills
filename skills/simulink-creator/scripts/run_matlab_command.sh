#!/bin/bash

# This tool check if matlab is available and run a matlab command.
# Usage with commands: ./run_matlab_command.sh "matlab command"
# Usage with files: ./run_matlab_command.sh "matlab filename (without extension)"
# Note: ensure the file has the right privileges to run, otherwise run `chmod +x run_matlab_command.sh`

# Check if matlab is available
if ! command -v matlab >/dev/null 2>&1; then
    echo "MATLAB is not available"
    exit 1
fi

# Run the matlab command
matlab -batch "$1"
