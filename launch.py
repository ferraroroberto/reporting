#!/usr/bin/env python
"""
Data Processing Project - Main Launcher
This is the main entry point for the application that launches the CLI interface.
The CLI provides access to all project functionalities including the social media pipeline.
"""

import sys
import os
from pathlib import Path

def main():
    """Main launcher function that starts the CLI."""
    print("🚀 Data Processing Project - Main Launcher")
    print("=" * 50)
    print("Launching the Command Line Interface...")
    print("=" * 50)
    
    # Get the project root directory
    project_root = Path(__file__).parent
    
    # Add the project root to Python path
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))
    
    try:
        # Import and launch the CLI
        from cli.main import main as cli_main
        cli_main()
    except ImportError as e:
        print(f"❌ Error importing CLI: {e}")
        print("Please make sure the CLI module is properly installed.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()