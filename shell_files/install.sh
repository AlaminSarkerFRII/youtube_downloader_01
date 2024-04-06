#!/bin/bash

# Check if Python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed. Please install Python3."
    exit 1
fi

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install required Python packages
pip install -r requirements.txt

# Install ffmpeg
if [[ "$(uname)" == "Linux" ]]; then
    # For Linux systems
    sudo apt-get update
    sudo apt-get install ffmpeg
elif [[ "$(uname)" == "Darwin" ]]; then
    # For macOS systems
    brew install ffmpeg
fi

# Deactivate virtual environment
deactivate

echo "Installation completed successfully."
