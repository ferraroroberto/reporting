# 🚀 CLI Quick Start Guide

## ⚡ Get Started in 30 Seconds

### 1. Launch the CLI
```bash
# From the project root
python3 cli/main.py

# Or use the launcher script (from anywhere)
./cli/launch.sh

# Or use the Python launcher
python3 cli/run.py
```

### 2. Choose Your Operation
The CLI will show you a menu with 8 options:

- **🚀 Option 1**: Run Default Pipeline (API → Notion) - **RECOMMENDED FOR FIRST USE**
- **📊 Option 2**: Show All Available Modules
- **🔍 Option 3**: Analyze Project Structure
- **⚙️ Option 4**: Run Custom Module
- **📋 Option 5**: Show Module Dependencies
- **🎯 Option 6**: Run Specific Workflow
- **❓ Option 7**: Help & Information
- **🚪 Option 8**: Exit

### 3. First Time? Choose Option 1!
This will run the complete pipeline:
1. Collect data from social media APIs
2. Process and transform the data
3. Aggregate profiles and posts
4. Sync everything to Notion

## 🎯 What Each Option Does

### 🚀 Default Pipeline (Option 1)
- **Best for**: Daily operations, complete data sync
- **What it does**: Runs the full pipeline from API collection to Notion update
- **Time**: 15-30 minutes
- **When to use**: When you want fresh data and complete synchronization

### 📊 Show All Modules (Option 2)
- **Best for**: Understanding what's available
- **What it shows**: All modules organized by category (Input, Processing, Output, Sync)
- **Use case**: Learning about the system capabilities

### 🔍 Analyze Structure (Option 3)
- **Best for**: Planning operations, understanding dependencies
- **What it shows**: Module dependencies, execution order, recommended plans
- **Use case**: Before running custom operations

### ⚙️ Run Custom Module (Option 4)
- **Best for**: Running specific parts of the system
- **What it does**: Lets you run individual modules
- **Use case**: When you only need specific functionality

### 📋 Show Dependencies (Option 5)
- **Best for**: Understanding module relationships
- **What it shows**: Tree structure of module dependencies
- **Use case**: Troubleshooting, planning execution order

### 🎯 Run Specific Workflow (Option 6)
- **Best for**: Common operation patterns
- **Available workflows**:
  - Data Collection Only
  - Data Processing Only
  - Notion Sync Only
  - Database Sync
  - Full Data Pipeline

### ❓ Help & Information (Option 7)
- **Best for**: Learning about the CLI
- **What it shows**: Usage tips, module categories, troubleshooting

## 🔄 Typical Usage Patterns

### Daily Operation
```bash
# Launch CLI
python3 cli/main.py

# Choose Option 1 (Default Pipeline)
# Wait for completion
# Done!
```

### Data Collection Only
```bash
# Launch CLI
python3 cli/main.py

# Choose Option 6 (Workflows)
# Choose Workflow 1 (Data Collection)
# Wait 5-10 minutes
# Done!
```

### Troubleshooting
```bash
# Launch CLI
python3 cli/main.py

# Choose Option 3 (Analyze Structure)
# Review dependencies and execution order
# Choose Option 5 (Show Dependencies)
# Identify potential issues
```

## ⚠️ Important Notes

1. **Dependencies Matter**: Some modules require others to run first
2. **Check Structure**: Use Option 3 before running custom operations
3. **Default is Safe**: Option 1 handles everything in the correct order
4. **Logs Available**: All operations are logged for debugging
5. **Can Interrupt**: Use Ctrl+C to stop operations safely

## 🆘 Need Help?

- **Option 7**: Built-in help and information
- **README.md**: Detailed documentation
- **Test Script**: Run `python3 cli/test_cli.py` to verify setup
- **Check Logs**: Look for error messages in the output

## 🎉 You're Ready!

The CLI is designed to be intuitive and safe. Start with Option 1 (Default Pipeline) and explore other options as you become familiar with the system.

**Happy data processing! 🚀**