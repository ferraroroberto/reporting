#!/usr/bin/env python
"""
Simple launcher script for the CLI
Can be run from any directory
"""

import os
import sys
from pathlib import Path

# Get the directory where this script is located
cli_dir = Path(__file__).parent
project_root = cli_dir.parent

# Add the project root to Python path
sys.path.insert(0, str(project_root))

# Change to the project root directory
os.chdir(project_root)

# Import and run the CLI
from cli.main import main

if __name__ == "__main__":
    main()