# Process Modules

This directory contains all the data processing modules for the Data Processing Project.

## 📁 Available Modules

### 🔄 Data Processing
- **`data_processor.py`** - Main data processing and transformation engine
- **`profile_aggregator.py`** - Aggregates profile data across different platforms
- **`posts_consolidator.py`** - Consolidates posts data across different platforms

### 🚀 Pipeline Orchestration
- **`social_media_pipeline.py`** - Complete social media data processing pipeline (API → Notion)

### 📤 Data Output
- **`supabase_uploader.py`** - Uploads processed data to Supabase database
- **`supabase_relations_creator.py`** - Creates database relations and structures
- **`supabase_policy_script.py`** - Manages database policies and security

### 🧪 Testing & Utilities
- **`supabase_test_connect.py`** - Tests database connectivity
- **`supabase_test_create_table.py`** - Tests table creation
- **`supabase_drop_all_tables.py`** - Utility for dropping all tables (use with caution!)

## 🚀 Social Media Pipeline

The **`social_media_pipeline.py`** is the main orchestration module that runs the complete data processing flow:

1. **Social API Client** - Collects data from social media APIs
2. **Data Processor** - Transforms and cleans raw data
3. **Profile Aggregator** - Aggregates profile information across platforms
4. **Posts Consolidator** - Consolidates posts data across platforms
5. **Notion Update** - Synchronizes processed data to Notion databases

### Usage

```bash
# Run the complete pipeline
python3 process/social_media_pipeline.py

# Run with debug mode
python3 process/social_media_pipeline.py --debug

# Skip specific steps
python3 process/social_media_pipeline.py --skip-api --skip-processing

# Specify a date
python3 process/social_media_pipeline.py --date 20241201
```

### Command Line Options

- `-d, --debug`: Enable debug mode for detailed logging
- `-s, --skip-api`: Skip the API data collection step
- `-p, --skip-processing`: Skip the data processing step
- `-a, --skip-aggregation`: Skip the profile aggregation step
- `-c, --skip-consolidation`: Skip the posts consolidation step
- `-n, --skip-notion`: Skip the Notion update step
- `--date`: Reference date in YYYYMMDD format

## 🔗 Dependencies

The modules have the following dependency chain:

```
social_api_client → data_processor → [profile_aggregator, posts_consolidator] → notion_update
```

## 📊 Data Flow

```
Raw API Data → Data Processing → Aggregation → Consolidation → Notion/Supabase
     ↓              ↓              ↓            ↓              ↓
API Client → Data Processor → Aggregators → Consolidators → Output Modules
```

## 🛠️ Development

### Adding New Modules

1. Create your module in this directory
2. Ensure it has a `main()` function
3. Add it to the CLI configuration in `cli/config.py`
4. Update dependencies if needed
5. Test the module integration

### Module Structure

Each module should:
- Have a clear, descriptive name
- Include proper error handling
- Use the logging system
- Have a `main()` function for CLI integration
- Include proper documentation

## 📝 Logging

All modules use the centralized logging system from `config/logger_config.py`. Use the `configure_logger()` function to set up logging for your module.

## 🔧 Configuration

Module configuration is managed through `cli/config.py`. This includes:
- Module definitions and metadata
- Dependencies and execution order
- Workflow definitions
- Execution plans

## 🚨 Important Notes

- **Dependencies Matter**: Always check module dependencies before running
- **Execution Order**: Use the CLI's structure analysis to understand execution order
- **Error Handling**: Failed modules are logged for debugging
- **Data Safety**: Some modules can modify or delete data - use with caution
