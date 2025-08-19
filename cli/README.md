# Command Line Interface (CLI) for Data Processing Project

This CLI provides an interactive interface to manage all the different functions and modules in your data processing project.

## 🚀 Quick Start

### Option 1: Run from project root
```bash
cd /path/to/your/project
python cli/main.py
```

### Option 2: Use the launcher script
```bash
python cli/run.py
```

### Option 3: Make it executable and run from anywhere
```bash
chmod +x cli/main.py
./cli/main.py
```

## 📋 Main Features

### 1. 🚀 Default Pipeline (API → Notion)
- **What it does**: Runs the complete data processing pipeline
- **Flow**: Social API Client → Data Processing → Profile Aggregation → Posts Consolidation → Notion Update
- **Use case**: When you want to collect fresh data and sync everything to Notion
- **Estimated time**: 15-30 minutes

### 2. 📊 Module Discovery
- Shows all available modules organized by category
- Displays module descriptions, types, and dependencies
- Helps you understand what each module does

### 3. 🔍 Project Structure Analysis
- Analyzes module dependencies
- Finds valid execution order using topological sorting
- Proposes recommended execution plans
- Estimates execution time for different workflows

### 4. ⚙️ Custom Module Execution
- Run any individual module selectively
- Checks dependencies before execution
- Provides safety confirmations

### 5. 📋 Dependency Visualization
- Shows module dependencies in a tree structure
- Helps understand the relationship between modules
- Identifies potential execution issues

### 6. 🎯 Predefined Workflows
- **Data Collection**: Just collect data from APIs
- **Data Processing**: Process existing collected data
- **Notion Sync**: Sync processed data to Notion
- **Database Sync**: Sync between Notion and Supabase

## 🏗️ Module Categories

### Input Modules
- **Social API Client**: Collects data from social media APIs
- **External Data Sources**: Any other data collection modules

### Processing Modules
- **Data Processor**: Transforms and cleans raw data
- **Profile Aggregator**: Aggregates profile data across platforms
- **Posts Consolidator**: Consolidates posts data across platforms

### Output Modules
- **Notion Update**: Updates Notion databases
- **Supabase Uploader**: Uploads data to Supabase

### Sync Modules
- **Notion-Supabase Sync**: Synchronizes between databases

## 🔄 Execution Flow

The CLI understands the natural flow of data processing:

```
Social APIs → Raw Data → Processed Data → Aggregated Data → Notion/Supabase
     ↓              ↓           ↓              ↓              ↓
API Client → Data Processor → Aggregators → Consolidators → Sync Modules
```

## ⚠️ Important Notes

### Dependencies
- Always check dependencies before running individual modules
- Some modules require others to run first
- The CLI will warn you about missing dependencies

### Execution Order
- The CLI automatically determines the correct execution order
- Use the structure analysis to understand the flow
- Follow the recommended execution plans

### Error Handling
- The CLI provides detailed error messages
- Failed modules are logged for debugging
- You can continue with other operations even if some fail

## 🛠️ Advanced Usage

### Debug Mode
Some modules support debug mode for detailed logging:
```python
# In the module code
if args.debug:
    logging.getLogger().setLevel(logging.DEBUG)
```

### Custom Arguments
You can pass custom arguments to modules when running them individually:
```python
# The CLI handles argument passing automatically
run_module(module_func, module_name, debug_mode, extra_args)
```

### Logging
- All operations are logged
- Check the logs for detailed execution information
- Use debug mode for troubleshooting

## 🔧 Troubleshooting

### Common Issues

1. **Import Errors**
   - Make sure you're running from the project root
   - Check that all dependencies are installed
   - Verify Python path configuration

2. **Module Not Found**
   - Check if the module file exists
   - Verify the module path in the CLI configuration
   - Ensure the module has a `main()` function

3. **Dependency Issues**
   - Run the structure analysis to understand dependencies
   - Execute modules in the correct order
   - Check if required data files exist

4. **Permission Errors**
   - Make sure the CLI scripts are executable
   - Check file permissions
   - Verify directory access rights

### Getting Help

- Use option 7 (Help & Information) in the main menu
- Check the README files in each module directory
- Review the logs for detailed error information
- Use debug mode for troubleshooting

## 📁 File Structure

```
cli/
├── main.py          # Main CLI interface
├── run.py           # Launcher script
└── README.md        # This file
```

## 🚀 Future Enhancements

The CLI is designed to be extensible. You can easily add:

- New modules by updating the `_discover_modules()` method
- Custom workflows by extending the workflows list
- Additional analysis tools
- Configuration management
- Batch operations
- Scheduled execution

## 🤝 Contributing

To add new modules to the CLI:

1. Update the `_discover_modules()` method in `main.py`
2. Add the module to the appropriate category
3. Define dependencies correctly
4. Test the module execution
5. Update this README if needed

## 📞 Support

If you encounter issues:

1. Check the logs for error details
2. Verify module dependencies
3. Test individual modules
4. Review the project structure
5. Check the main project README for module-specific information