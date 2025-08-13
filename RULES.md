# RULES.md - Coding Standards & Project Organization

This document defines the coding standards, architectural patterns, and organizational principles derived from the analysis of the current codebase. These rules should be applied to all future development to maintain consistency and quality.

## 📁 Project Structure & Organization

### Directory Structure
```
project_root/
├── config/                 # Configuration files and utilities
├── social_client/          # API client modules
├── process/               # Data processing and database operations
├── notion/                # External service integrations
├── results/               # Output directories (raw/processed)
├── logs/                  # Log files (auto-generated)
├── requirements.txt       # Python dependencies
├── init.py               # Main orchestration script
└── README.md             # Project documentation
```

### Module Organization Rules
- **Separate concerns**: Each major functionality gets its own directory
- **Clear naming**: Use descriptive, lowercase names with underscores
- **Hierarchical structure**: Group related functionality together
- **Configuration separation**: Keep all config files in a dedicated `config/` directory

## 🐍 Python Coding Standards

### Import Organization
```python
# Standard library imports first
import json
import os
import sys
from datetime import datetime
from pathlib import Path

# Third-party imports
import requests
import pandas as pd

# Local imports (with path manipulation for sibling packages)
sys.path.append(str(Path(__file__).parent.parent))
from config.logger_config import setup_logger
```

### Import Rules
1. **Order**: Standard library → Third-party → Local imports
2. **Path handling**: Use `sys.path.append()` for sibling package imports
3. **Explicit imports**: Avoid wildcard imports (`from module import *`)
4. **Relative paths**: Use `Path(__file__).parent` for file path resolution

### Function and Variable Naming
```python
# Functions: lowercase with underscores
def load_config():
    pass

def get_nested_value(data, path):
    pass

# Variables: lowercase with underscores
config_dir = os.path.join(os.path.dirname(__file__), 'config')
api_config = config[platform_key]

# Constants: UPPERCASE with underscores
MAX_RETRIES = 5
BACKOFF_TIMES = [30, 60, 120, 240, 480]
```

### Naming Conventions
- **Functions**: `snake_case` (e.g., `load_config`, `get_nested_value`)
- **Variables**: `snake_case` (e.g., `config_dir`, `api_config`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `MAX_RETRIES`)
- **Classes**: `PascalCase` (e.g., `DataProcessor`)
- **Files**: `snake_case.py` (e.g., `data_processor.py`)

## 🔧 Configuration Management

### Configuration File Structure
```json
{
    "folder_results_raw": "results/raw",
    "folder_results_processed": "results/processed",
    "supabase": {
        "environment": "cloud",
        "url": "your_supabase_url_here",
        "key": "your_supabase_key_here"
    },
    "platform_name": {
        "api_url": "https://api.example.com/endpoint",
        "api_key": "your_api_key_here",
        "api_host": "api.example.com",
        "querystring": {
            "param1": "value1"
        }
    }
}
```

### Configuration Rules
1. **Hierarchical structure**: Group related settings under logical keys
2. **Environment separation**: Use separate configs for different environments
3. **Sensitive data**: Never commit API keys or credentials to version control
4. **Example files**: Provide `config_example.json` for reference
5. **Validation**: Always validate config file existence and JSON format

### Configuration Loading Pattern
```python
def load_config():
    """Load configuration from config.json file."""
    logger.debug("📂 Loading configuration file")
    config_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config')
    config_path = os.path.join(config_dir, 'config.json')
    
    try:
        with open(config_path, 'r') as file:
            logger.info("✅ Configuration loaded successfully")
            return json.load(file)
    except FileNotFoundError:
        logger.error(f"❌ Error: Configuration file not found at {config_path}")
        return None
    except json.JSONDecodeError:
        logger.error(f"❌ Error: Invalid JSON in configuration file at {config_path}")
        return None
```

## 📝 Logging Standards

### Logger Configuration
```python
def configure_logger(debug_mode=False):
    """Set up logger with appropriate level based on debug mode."""
    global logger
    log_level = logging.DEBUG if debug_mode else logging.INFO
    logger = setup_logger("module_name", file_logging=False, level=level)
    return logger
```

### Logging Rules
1. **Centralized setup**: Use `config/logger_config.py` for all logging configuration
2. **Debug mode**: Support `--debug` flag for verbose logging
3. **Emoji prefixes**: Use emojis for visual log categorization
   - 📂 File operations
   - ✅ Success messages
   - ❌ Error messages
   - 🔍 Search/query operations
   - 📡 API calls
   - ⏳ Waiting/retry operations
4. **Consistent format**: Use structured logging with timestamps
5. **File logging**: Support both console and file output

### Log Message Examples
```python
logger.debug("📂 Loading configuration file")
logger.info("✅ Configuration loaded successfully")
logger.error(f"❌ Error: Configuration file not found at {config_path}")
logger.info(f"🔍 Fetching {platform_key} data")
logger.info(f"⏳ Retrying in {wait_time} seconds...")
```

## 🚀 Error Handling & Resilience

### Retry Pattern with Exponential Backoff
```python
def get_api_data(platform_key, config):
    """Fetch data using the API with retries and exponential backoff."""
    retries = 5
    backoff_times = [30, 60, 120, 240, 480]  # seconds

    for attempt in range(retries):
        try:
            logger.debug(f"📡 Making API request (attempt {attempt+1}/{retries})")
            response = requests.get(url, headers=headers, params=querystring)
            response.raise_for_status()
            logger.info(f"✅ Successfully retrieved {platform_key} data")
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"❌ Error fetching data (attempt {attempt+1}/{retries}): {e}")
            if attempt < retries - 1:
                wait_time = backoff_times[attempt]
                logger.info(f"⏳ Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
    
    return None
```

### Error Handling Rules
1. **Graceful degradation**: Handle errors without crashing the application
2. **Retry logic**: Implement exponential backoff for transient failures
3. **Detailed logging**: Log errors with context and attempt information
4. **User feedback**: Provide clear error messages and recovery suggestions
5. **Exception types**: Catch specific exceptions rather than generic ones

## 🔄 Data Processing Patterns

### Data Transformation Functions
```python
def get_nested_value(data, path):
    """Extract value from nested dictionary using dot notation path."""
    try:
        keys = path.split('.')
        value = data
        for key in keys:
            if key.isdigit():
                key = int(key)
            
            if isinstance(value, dict) and key in value:
                value = value[key]
            elif isinstance(value, list) and isinstance(key, int) and key < len(value):
                value = value[key]
            else:
                return None
                
        return value
    except (KeyError, TypeError, IndexError) as e:
        logger.debug(f"Error accessing path {path}: {str(e)}")
        return None
```

### Data Processing Rules
1. **Type safety**: Always validate data types before processing
2. **Null handling**: Gracefully handle missing or null values
3. **Path notation**: Use dot notation for nested data access
4. **Error logging**: Log data access errors at debug level
5. **Data validation**: Validate data structure before processing

## 🗄️ Database Operations

### Database Connection Pattern
```python
def get_db_connection():
    """Get database connection with environment-based configuration."""
    load_dotenv()
    
    if os.getenv('ENVIRONMENT') == 'local':
        # Local PostgreSQL connection
        return psycopg2.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
    else:
        # Supabase connection
        return psycopg2.connect(
            host=os.getenv('SUPABASE_HOST'),
            database=os.getenv('SUPABASE_DB'),
            user=os.getenv('SUPABASE_USER'),
            password=os.getenv('SUPABASE_PASSWORD')
        )
```

### Database Rules
1. **Environment separation**: Support both local and cloud database configurations
2. **Connection pooling**: Implement connection management for efficiency
3. **Transaction handling**: Use proper transaction boundaries
4. **Error handling**: Handle database connection failures gracefully
5. **SQL files**: Keep complex SQL queries in separate `.sql` files

## 🚀 Command Line Interface

### Argument Parsing Pattern
```python
def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Module description.')
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug mode')
    parser.add_argument('--skip-existing', action='store_true', help='Skip existing data')
    parser.add_argument('--date', type=str, help='Reference date in YYYYMMDD format')
    return parser.parse_args()
```

### CLI Rules
1. **Standard flags**: Always support `--debug` for verbose logging
2. **Descriptive help**: Provide clear help text for all arguments
3. **Date formats**: Use `YYYYMMDD` format for date parameters
4. **Skip options**: Provide flags to skip specific processing steps
5. **Argument validation**: Validate input parameters before processing

## 📊 File Management

### File Naming Convention
```python
# Date-based file naming
current_date = datetime.now().strftime('%Y-%m-%d')
filename = f"{platform}_{data_type}_{current_date}.json"

# Directory structure
results_dir = os.path.join(project_root, *results_dir_relative.split('/'))
file_path = os.path.join(results_dir, filename)
```

### File Management Rules
1. **Date-based naming**: Use `YYYY-MM-DD` format for daily files
2. **Platform prefixes**: Include platform name in filenames
3. **Directory creation**: Auto-create directories if they don't exist
4. **Path handling**: Use `os.path.join()` for cross-platform compatibility
5. **File existence checks**: Check for existing files to avoid duplicates

## 🔐 Security & Environment Variables

### Environment Variable Pattern
```python
# Load environment variables
load_dotenv()

# Access sensitive configuration
api_key = os.getenv('API_KEY')
database_url = os.getenv('DATABASE_URL')
```

### Security Rules
1. **Never hardcode**: Never commit API keys or credentials to version control
2. **Environment files**: Use `.env` files for local development
3. **Example files**: Provide `.env_example` for reference
4. **Access control**: Use read-only database users where possible
5. **Key rotation**: Implement regular API key rotation

## 📚 Documentation Standards

### README Structure
```markdown
# Module Name

Brief description of the module's purpose.

## 🚀 Overview

Detailed explanation of functionality.

## 📋 Usage

Code examples and usage instructions.

## 🔧 Configuration

Configuration options and examples.

## 📊 Output

Description of output format and structure.
```

### Documentation Rules
1. **Emoji headers**: Use emojis for visual section identification
2. **Code examples**: Provide practical usage examples
3. **Configuration docs**: Document all configuration options
4. **Output format**: Describe data structures and formats
5. **Troubleshooting**: Include common issues and solutions

## 🧪 Testing & Debugging

### Debug Mode Pattern
```python
def main():
    args = parse_arguments()
    logger = configure_logger(args.debug)
    
    if args.debug:
        logger.debug("🐞 Debug mode enabled")
        # Additional debug logging
```

### Debug Rules
1. **Debug flag**: Always support `--debug` command line flag
2. **Verbose logging**: Provide detailed information in debug mode
3. **Error details**: Show full error traces in debug mode
4. **State inspection**: Log internal state and data structures
5. **Performance metrics**: Log timing information in debug mode

## 🔄 Pipeline Orchestration

### Main Script Pattern
```python
def main():
    """Main execution function."""
    args = parse_arguments()
    logger = configure_logger(args.debug)
    
    try:
        # Load configuration
        config = load_config()
        if not config:
            logger.error("❌ Failed to load configuration")
            return 1
        
        # Execute main logic
        result = process_data(config, args)
        
        if result:
            logger.info("✅ Processing completed successfully")
            return 0
        else:
            logger.error("❌ Processing failed")
            return 1
            
    except Exception as e:
        logger.error(f"❌ Unexpected error: {e}")
        if args.debug:
            raise
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

### Orchestration Rules
1. **Main function**: Always wrap main logic in a `main()` function
2. **Exit codes**: Return appropriate exit codes (0 for success, 1 for failure)
3. **Exception handling**: Catch and log all exceptions
4. **Debug mode**: Re-raise exceptions in debug mode for full traceback
5. **Configuration validation**: Validate configuration before processing

## 📦 Dependency Management

### Requirements.txt Rules
```txt
# Package with version pinning
requests==2.31.0
pandas==2.2.2
notion-client==2.2.1

# Include purpose comments
# For making HTTP requests (used for API calls)
requests==2.31.0
```

### Dependency Rules
1. **Version pinning**: Pin exact versions for reproducibility
2. **Purpose comments**: Document why each dependency is needed
3. **Minimal dependencies**: Only include necessary packages
4. **Security updates**: Regularly update dependencies for security patches
5. **Virtual environments**: Use virtual environments for isolation

## 🚧 Development Workflow

### Adding New Features
1. **Follow structure**: Adhere to established directory and file organization
2. **Configuration first**: Add configuration options before implementing features
3. **Logging**: Implement comprehensive logging from the start
4. **Error handling**: Plan error handling and recovery strategies
5. **Documentation**: Update README and add inline documentation

### Code Review Checklist
- [ ] Follows naming conventions
- [ ] Includes proper error handling
- [ ] Has comprehensive logging
- [ ] Includes debug mode support
- [ ] Follows configuration patterns
- [ ] Has proper documentation
- [ ] Includes appropriate exit codes
- [ ] Handles edge cases gracefully

## 📋 Summary of Key Principles

1. **Consistency**: Follow established patterns throughout the codebase
2. **Reliability**: Implement robust error handling and retry logic
3. **Observability**: Comprehensive logging and debug capabilities
4. **Configuration**: Centralized, environment-aware configuration management
5. **Modularity**: Clear separation of concerns and responsibilities
6. **Documentation**: Comprehensive documentation with practical examples
7. **Security**: Never commit sensitive data, use environment variables
8. **Maintainability**: Clean, readable code with consistent formatting

---

*This document is derived from the analysis of the existing codebase and should be updated as new patterns and standards emerge.*