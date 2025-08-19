#!/usr/bin/env python
"""
Configuration file for the CLI
Contains module definitions, workflows, and settings
"""

from typing import Dict, List, Any

# CLI Configuration
CLI_CONFIG = {
    "name": "Data Processing Project CLI",
    "version": "1.0.0",
    "description": "Command Line Interface for managing data processing operations",
    "default_timeout": 300,  # 5 minutes default timeout
    "enable_logging": True,
    "log_level": "INFO"
}

# Module Definitions
# Each module should have: name, description, path, type, dependencies, category
MODULES = {
    "social_api_client": {
        "name": "Social API Client",
        "description": "Collect data from social media APIs",
        "path": "social_client/social_api_client.py",
        "type": "data_collection",
        "dependencies": [],
        "category": "input",
        "estimated_time": "5-10 minutes",
        "enabled": True
    },
    "data_processor": {
        "name": "Data Processor",
        "description": "Process and transform raw data",
        "path": "process/data_processor.py",
        "type": "data_processing",
        "dependencies": ["social_api_client"],
        "category": "processing",
        "estimated_time": "5-10 minutes",
        "enabled": True
    },
    "profile_aggregator": {
        "name": "Profile Aggregator",
        "description": "Aggregate profile data across platforms",
        "path": "process/profile_aggregator.py",
        "type": "data_aggregation",
        "dependencies": ["data_processor"],
        "category": "processing",
        "estimated_time": "3-5 minutes",
        "enabled": True
    },
    "posts_consolidator": {
        "name": "Posts Consolidator",
        "description": "Consolidate posts data across platforms",
        "path": "process/posts_consolidator.py",
        "type": "data_consolidation",
        "dependencies": ["data_processor"],
        "category": "processing",
        "estimated_time": "3-5 minutes",
        "enabled": True
    },
    "notion_update": {
        "name": "Notion Update",
        "description": "Update Notion databases with processed data",
        "path": "notion/notion_update.py",
        "type": "data_sync",
        "dependencies": ["profile_aggregator", "posts_consolidator"],
        "category": "output",
        "estimated_time": "5-10 minutes",
        "enabled": True
    },
    "notion_supabase_sync": {
        "name": "Notion-Supabase Sync",
        "description": "Synchronize data between Notion and Supabase",
        "path": "notion/notion_supabase_sync.py",
        "type": "data_sync",
        "dependencies": ["notion_update"],
        "category": "sync",
        "estimated_time": "5-10 minutes",
        "enabled": True
    },
    "supabase_uploader": {
        "name": "Supabase Uploader",
        "description": "Upload data to Supabase database",
        "path": "process/supabase_uploader.py",
        "type": "data_upload",
        "dependencies": ["data_processor"],
        "category": "output",
        "estimated_time": "3-5 minutes",
        "enabled": True
    },
    "social_media_pipeline": {
        "name": "Social Media Pipeline",
        "description": "Complete social media data processing pipeline (API → Notion)",
        "path": "process/social_media_pipeline.py",
        "type": "pipeline",
        "dependencies": ["social_api_client", "data_processor", "profile_aggregator", "posts_consolidator", "notion_update"],
        "category": "pipeline",
        "estimated_time": "15-30 minutes",
        "enabled": True
    }
}

# Predefined Workflows
WORKFLOWS = [
    {
        "id": "1",
        "name": "Data Collection Workflow",
        "description": "Collect data from all APIs",
        "modules": ["social_api_client"],
        "estimated_time": "5-10 minutes",
        "category": "collection"
    },
    {
        "id": "2", 
        "name": "Data Processing Workflow",
        "description": "Process collected data",
        "modules": ["data_processor", "profile_aggregator", "posts_consolidator"],
        "estimated_time": "10-15 minutes",
        "category": "processing"
    },
    {
        "id": "3",
        "name": "Notion Sync Workflow", 
        "description": "Sync data to Notion",
        "modules": ["notion_update"],
        "estimated_time": "5-10 minutes",
        "category": "sync"
    },
    {
        "id": "4",
        "name": "Database Sync Workflow",
        "description": "Sync between databases",
        "modules": ["notion_supabase_sync"],
        "estimated_time": "5-10 minutes",
        "category": "sync"
    },
    {
        "id": "5",
        "name": "Social Media Pipeline",
        "description": "Complete social media data processing (API → Notion)",
        "modules": ["social_media_pipeline"],
        "estimated_time": "15-30 minutes",
        "category": "pipeline"
    }
]

# Category Information
CATEGORIES = {
    "input": {
        "name": "Input Modules",
        "description": "Data collection from external sources",
        "icon": "📥",
        "color": "blue"
    },
    "processing": {
        "name": "Processing Modules", 
        "description": "Data transformation and aggregation",
        "icon": "⚙️",
        "color": "green"
    },
    "output": {
        "name": "Output Modules",
        "description": "Data export to external systems",
        "icon": "📤",
        "color": "yellow"
    },
    "sync": {
        "name": "Sync Modules",
        "description": "Synchronization between systems",
        "icon": "🔄",
        "color": "purple"
    },
    "pipeline": {
        "name": "Pipeline Modules",
        "description": "Complete end-to-end data processing pipelines",
        "icon": "🚀",
        "color": "orange"
    }
}

# Execution Plans
EXECUTION_PLANS = [
    {
        "name": "Social Media Pipeline",
        "description": "Complete social media data processing (API → Notion)",
        "modules": ["social_media_pipeline"],
        "estimated_time": "15-30 minutes",
        "recommended": True
    },
    {
        "name": "Data Collection Only",
        "description": "Just collect data from APIs",
        "modules": ["social_api_client"],
        "estimated_time": "5-10 minutes",
        "recommended": False
    },
    {
        "name": "Data Processing Only",
        "description": "Process existing collected data",
        "modules": ["data_processor", "profile_aggregator", "posts_consolidator"],
        "estimated_time": "10-15 minutes",
        "recommended": False
    },
    {
        "name": "Notion Sync Only",
        "description": "Sync processed data to Notion",
        "modules": ["notion_update"],
        "estimated_time": "5-10 minutes",
        "recommended": False
    },
    {
        "name": "Database Sync",
        "description": "Sync between Notion and Supabase",
        "modules": ["notion_supabase_sync"],
        "estimated_time": "5-10 minutes",
        "recommended": False
    }
]

# UI Configuration
UI_CONFIG = {
    "show_emojis": True,
    "show_colors": True,
    "show_progress_bars": True,
    "confirm_destructive_actions": True,
    "auto_continue_on_success": False,
    "max_display_width": 80
}

# Logging Configuration
LOGGING_CONFIG = {
    "file_logging": False,
    "console_logging": True,
    "log_level": "INFO",
    "log_format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "date_format": "%Y-%m-%d %H:%M:%S"
}

def get_enabled_modules() -> Dict[str, Dict[str, Any]]:
    """Get only enabled modules."""
    return {k: v for k, v in MODULES.items() if v.get("enabled", True)}

def get_modules_by_category(category: str) -> Dict[str, Dict[str, Any]]:
    """Get modules filtered by category."""
    enabled_modules = get_enabled_modules()
    return {k: v for k, v in enabled_modules.items() if v.get("category") == category}

def get_workflows_by_category(category: str) -> List[Dict[str, Any]]:
    """Get workflows filtered by category."""
    return [w for w in WORKFLOWS if w.get("category") == category]

def get_recommended_plans() -> List[Dict[str, Any]]:
    """Get only recommended execution plans."""
    return [p for p in EXECUTION_PLANS if p.get("recommended", False)]