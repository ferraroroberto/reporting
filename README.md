# Data Processing Project

A comprehensive data processing system that collects, processes, and synchronizes social media data across multiple platforms and databases.

## 🚀 Quick Start

### Launch the Application
```bash
# Main launcher (recommended)
python3 launch.py

# Direct CLI access
python3 cli/main.py

# Alternative launchers
./cli/launch.sh
python3 cli/run.py
```

### Default Operation
The CLI will start and show you a menu. **Choose Option 1** to run the default social media pipeline that:
1. Collects data from social media APIs
2. Processes and transforms the data
3. Syncs everything to your Notion base

## 🏗️ Project Structure

```
├── launch.py                    # 🚀 Main application launcher
├── cli/                        # 🖥️ Command Line Interface
│   ├── main.py                 # Main CLI interface
│   ├── config.py               # Module configuration
│   ├── run.py                  # Python launcher
│   └── launch.sh               # Bash launcher
├── social_client/              # 📡 Social Media API Clients
│   └── social_api_client.py    # Data collection from APIs
├── process/                    # ⚙️ Data Processing & Pipelines
│   ├── social_media_pipeline.py # 🚀 Complete pipeline (API → Notion)
│   ├── data_processor.py       # Data transformation engine
│   ├── profile_aggregator.py   # Profile data aggregation
│   ├── posts_consolidator.py   # Posts data consolidation
│   └── supabase_uploader.py    # Database uploads
├── notion/                     # 📘 Notion Integration
│   ├── notion_update.py        # Update Notion databases
│   └── notion_supabase_sync.py # Sync between Notion & Supabase
├── config/                     # ⚙️ Configuration Files
│   ├── logger_config.py        # Logging configuration
│   └── mapping.json            # Data field mappings
└── requirements.txt            # 📦 Python dependencies
```

## 🎯 Main Features

### 🚀 **Social Media Pipeline** (Default Operation)
- **Complete end-to-end processing**: From API collection to Notion synchronization
- **Multi-platform support**: Handles data from various social media platforms
- **Automated workflow**: Runs all steps in the correct dependency order
- **Configurable**: Skip specific steps or customize processing

### 🖥️ **Command Line Interface**
- **Interactive menu**: Easy-to-use interface for all operations
- **Module management**: Run individual modules or complete workflows
- **Structure analysis**: Understand dependencies and execution order
- **Predefined workflows**: Common operation patterns

### 📊 **Data Processing**
- **Raw data collection**: Automated API data fetching
- **Data transformation**: Clean and structure raw data
- **Cross-platform aggregation**: Consolidate data from multiple sources
- **Quality assurance**: Validation and error handling

### 🔄 **Synchronization**
- **Notion integration**: Update databases with processed data
- **Supabase sync**: Database synchronization and backup
- **Real-time updates**: Keep all systems in sync

## 🚀 Usage

### 1. **Launch the Application**
```bash
python3 launch.py
```

### 2. **Choose Your Operation**
The CLI presents 8 options:

- **🚀 Option 1**: Run Default Pipeline (API → Notion) - **RECOMMENDED**
- **📊 Option 2**: Show All Available Modules
- **🔍 Option 3**: Analyze Project Structure
- **⚙️ Option 4**: Run Custom Module
- **📋 Option 5**: Show Module Dependencies
- **🎯 Option 6**: Run Specific Workflow
- **❓ Option 7**: Help & Information
- **🚪 Option 8**: Exit

### 3. **First Time? Use Option 1!**
This runs the complete social media pipeline:
- Collects fresh data from APIs
- Processes and transforms the data
- Syncs everything to Notion
- Estimated time: 15-30 minutes

## 🔧 Configuration

### Environment Setup
1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure your environment variables (see `.env_example`)

3. Set up your Notion and Supabase credentials

### Module Configuration
All modules are configured through `cli/config.py`:
- Module definitions and metadata
- Dependencies and execution order
- Workflow definitions
- Execution plans

## 📊 Available Modules

### **Input Modules** 📥
- **Social API Client**: Collects data from social media APIs

### **Processing Modules** ⚙️
- **Data Processor**: Transforms and cleans raw data
- **Profile Aggregator**: Aggregates profile data across platforms
- **Posts Consolidator**: Consolidates posts data across platforms

### **Output Modules** 📤
- **Notion Update**: Updates Notion databases
- **Supabase Uploader**: Uploads data to Supabase

### **Sync Modules** 🔄
- **Notion-Supabase Sync**: Synchronizes between databases

### **Pipeline Modules** 🚀
- **Social Media Pipeline**: Complete end-to-end processing

## 🔄 Data Flow

```
Social APIs → Raw Data → Processed Data → Aggregated Data → Notion/Supabase
     ↓              ↓           ↓              ↓              ↓
API Client → Data Processor → Aggregators → Consolidators → Sync Modules
```

## 🛠️ Development

### Adding New Modules
1. Create your module in the appropriate directory
2. Ensure it has a `main()` function
3. Add it to `cli/config.py`
4. Define dependencies correctly
5. Test integration

### Extending the Pipeline
1. Add new processing steps to `process/social_media_pipeline.py`
2. Update dependencies in the configuration
3. Test the complete workflow
4. Update documentation

## 🚨 Important Notes

- **Dependencies Matter**: Some modules require others to run first
- **Use the CLI**: It automatically manages execution order
- **Check Structure**: Use Option 3 to understand dependencies
- **Default is Safe**: Option 1 handles everything correctly

## 🆘 Getting Help

- **Built-in Help**: Use Option 7 in the CLI
- **Documentation**: Check the README files in each directory
- **Structure Analysis**: Use Option 3 to understand the system
- **Module Details**: Use Option 2 to see all available modules

## 📝 Logging

All operations are logged with:
- Console output with emoji indicators
- Debug mode for troubleshooting
- Error tracking and reporting
- Progress monitoring

## 🔒 Security

- Environment-based configuration
- Secure credential management
- Database access controls
- Row-level security policies

## 🚀 Future Enhancements

The system is designed to be extensible:
- Add new data sources
- Implement additional processing steps
- Extend synchronization capabilities
- Add monitoring and alerting
- Support for real-time processing

## 🤝 Contributing

1. Follow the existing module structure
2. Update configuration files
3. Test your changes thoroughly
4. Update documentation
5. Use the CLI for testing

## 📞 Support

For issues and questions:
1. Check the CLI help (Option 7)
2. Review module documentation
3. Check logs for error details
4. Use the structure analysis (Option 3)

---

**🎉 Ready to process your data? Launch the application with `python3 launch.py` and choose Option 1!**
