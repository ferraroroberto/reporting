#!/bin/bash
"""
Simple launcher script for the CLI
Can be run from any directory
"""

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Change to the project root directory
cd "$PROJECT_ROOT"

# Check if Python 3 is available
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "❌ Error: Python 3 is not installed or not in PATH"
    exit 1
fi

# Check if the CLI files exist
if [ ! -f "$SCRIPT_DIR/main.py" ]; then
    echo "❌ Error: CLI main.py not found at $SCRIPT_DIR/main.py"
    exit 1
fi

if [ ! -f "$SCRIPT_DIR/config.py" ]; then
    echo "❌ Error: CLI config.py not found at $SCRIPT_DIR/config.py"
    exit 1
fi

echo "🚀 Launching Data Processing Project CLI..."
echo "📁 Project root: $PROJECT_ROOT"
echo "🐍 Using Python: $PYTHON_CMD"
echo ""

# Launch the CLI
"$PYTHON_CMD" "$SCRIPT_DIR/main.py"