#!/bin/bash

# Get the Python file name from the environment variable
script.py=$PYFILE

# Check if the filename is provided
if [ -z script.py]; then
  echo "Error: PYFILE environment variable is not set."
  exit 1
fi

# Check if the Python file exists
if [ ! -f script.py ]; then
  echo "Error: Python file '$filename' not found."
  exit 1
fi

# Run the Python script
python script.py

