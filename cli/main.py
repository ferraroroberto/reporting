#!/usr/bin/env python
"""
Command Line Interface (CLI) for the Data Processing Project
Provides an interactive menu to run different functions and modules
"""

import os
import sys
import json
import logging
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime

# Add the parent directory to the Python path
sys.path.append(str(Path(__file__).parent.parent))

try:
    from config.logger_config import setup_logger
except ImportError:
    # Fallback if config module is not available
    def setup_logger(name, file_logging=False, level=logging.INFO):
        logger = logging.getLogger(name)
        logger.setLevel(level)
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        return logger

from cli.config import MODULES, WORKFLOWS, EXECUTION_PLANS, CATEGORIES, CLI_CONFIG

class DataProcessingCLI:
    """Main CLI class for managing data processing operations."""
    
    def __init__(self):
        self.logger = setup_logger("cli", file_logging=False, level=logging.INFO)
        self.project_root = Path(__file__).parent.parent
        self.available_modules = MODULES
    
    def show_welcome(self):
        """Display welcome message and main menu."""
        print("\n" + "="*60)
        print("🚀 DATA PROCESSING PROJECT - COMMAND LINE INTERFACE")
        print("="*60)
        print(f"📅 Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"📁 Project root: {self.project_root}")
        print("="*60)
        
    def show_main_menu(self):
        """Display the main menu options."""
        print("\n📋 MAIN MENU:")
        print("1. 🚀 Run Default Pipeline (API → Notion)")
        print("2. 📊 Show All Available Modules")
        print("3. 🔍 Analyze Project Structure")
        print("4. ⚙️  Run Custom Module")
        print("5. 📋 Show Module Dependencies")
        print("6. 🎯 Run Specific Workflow")
        print("7. ❓ Help & Information")
        print("8. 🚪 Exit")
        print("-" * 40)
        
    def run_default_pipeline(self):
        """Run the default pipeline: API sync to Notion base."""
        print("\n🚀 RUNNING DEFAULT PIPELINE")
        print("This will execute: Social API Client → Data Processing → Notion Update")
        print("-" * 50)
        
        try:
            # Import and run the init pipeline
            from init import run_pipeline
            
            print("⏳ Starting pipeline execution...")
            run_pipeline(
                debug_mode=False,
                skip_api=False,
                skip_processing=False,
                skip_aggregation=False,
                skip_consolidation=False,
                skip_notion=False
            )
            print("✅ Default pipeline completed successfully!")
            
        except Exception as e:
            print(f"❌ Error running default pipeline: {e}")
            self.logger.error(f"Pipeline execution failed: {e}")
            
        input("\nPress Enter to continue...")
    
    def show_all_modules(self):
        """Display all available modules with their details."""
        print("\n📊 ALL AVAILABLE MODULES")
        print("=" * 80)
        
        categories = {}
        for module_id, module_info in self.available_modules.items():
            category = module_info["category"]
            if category not in categories:
                categories[category] = []
            categories[category].append((module_id, module_info))
        
        for category, modules in categories.items():
            category_info = CATEGORIES.get(category, {})
            icon = category_info.get('icon', '🔸')
            name = category_info.get('name', category.upper())
            description = category_info.get('description', '')
            
            print(f"\n{icon} {name}")
            if description:
                print(f"   {description}")
            print("-" * 40)
            
            for module_id, module_info in modules:
                print(f"  📁 {module_id}")
                print(f"     Name: {module_info['name']}")
                print(f"     Description: {module_info['description']}")
                print(f"     Type: {module_info['type']}")
                print(f"     Dependencies: {', '.join(module_info['dependencies']) if module_info['dependencies'] else 'None'}")
                if 'estimated_time' in module_info:
                    print(f"     Estimated time: {module_info['estimated_time']}")
                print()
        
        input("Press Enter to continue...")
    
    def analyze_project_structure(self):
        """Analyze the project structure and propose execution plans."""
        print("\n🔍 PROJECT STRUCTURE ANALYSIS")
        print("=" * 60)
        
        # Analyze dependencies
        print("\n📋 DEPENDENCY ANALYSIS:")
        print("-" * 30)
        
        dependency_graph = {}
        for module_id, module_info in self.available_modules.items():
            dependency_graph[module_id] = module_info["dependencies"]
        
        # Find execution order
        execution_order = self._topological_sort(dependency_graph)
        
        if execution_order:
            print("✅ Valid execution order found:")
            for i, module_id in enumerate(execution_order, 1):
                module_info = self.available_modules[module_id]
                print(f"  {i}. {module_info['name']} ({module_id})")
        else:
            print("❌ Circular dependency detected!")
        
        # Propose execution plans
        print("\n🎯 RECOMMENDED EXECUTION PLANS:")
        print("-" * 35)
        
        # Use execution plans from configuration
        for i, plan in enumerate(EXECUTION_PLANS, 1):
            print(f"\n  {i}. {plan['name']}")
            print(f"     Description: {plan['description']}")
            print(f"     Modules: {', '.join(plan['modules'])}")
            print(f"     Estimated time: {plan['estimated_time']}")
            if plan.get('recommended'):
                print(f"     ⭐ RECOMMENDED")
        
        input("\nPress Enter to continue...")
    
    def _topological_sort(self, graph: Dict[str, List[str]]) -> List[str]:
        """Perform topological sort to find valid execution order."""
        in_degree = {node: 0 for node in graph}
        
        # Calculate in-degrees
        for node in graph:
            for neighbor in graph[node]:
                if neighbor in in_degree:
                    in_degree[neighbor] += 1
        
        # Find nodes with no dependencies
        queue = [node for node in in_degree if in_degree[node] == 0]
        result = []
        
        while queue:
            node = queue.pop(0)
            result.append(node)
            
            for neighbor in graph.get(node, []):
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Check if all nodes were processed
        if len(result) != len(graph):
            return []  # Circular dependency
        
        return result
    
    def run_custom_module(self):
        """Allow user to run a specific module."""
        print("\n⚙️  RUN CUSTOM MODULE")
        print("=" * 30)
        
        # Show available modules
        print("Available modules:")
        for i, (module_id, module_info) in enumerate(self.available_modules.items(), 1):
            print(f"  {i}. {module_info['name']} ({module_id})")
        
        try:
            choice = input("\nEnter module number or ID: ").strip()
            
            # Try to find by number first
            if choice.isdigit():
                choice_idx = int(choice) - 1
                if 0 <= choice_idx < len(self.available_modules):
                    module_id = list(self.available_modules.keys())[choice_idx]
                else:
                    print("❌ Invalid module number!")
                    return
            else:
                if choice not in self.available_modules:
                    print(f"❌ Module '{choice}' not found!")
                    return
                module_id = choice
            
            module_info = self.available_modules[module_id]
            print(f"\n🚀 Running module: {module_info['name']}")
            print(f"Description: {module_info['description']}")
            
            # Check dependencies
            if module_info['dependencies']:
                print(f"⚠️  Dependencies: {', '.join(module_info['dependencies'])}")
                print("Make sure dependencies have been run first!")
            
            confirm = input("\nProceed? (y/N): ").strip().lower()
            if confirm != 'y':
                print("❌ Operation cancelled.")
                return
            
            # Run the module
            self._run_module(module_id, module_info)
            
        except ValueError:
            print("❌ Invalid input!")
        except KeyboardInterrupt:
            print("\n❌ Operation cancelled by user.")
        
        input("\nPress Enter to continue...")
    
    def _run_module(self, module_id: str, module_info: Dict[str, Any]):
        """Execute a specific module."""
        try:
            module_path = self.project_root / module_info["path"]
            
            if not module_path.exists():
                print(f"❌ Module file not found: {module_path}")
                return
            
            print(f"⏳ Executing {module_info['name']}...")
            
            # Import and run the module
            module_name = module_info["path"].replace("/", ".").replace(".py", "")
            if module_name.startswith("."):
                module_name = module_name[1:]
            
            # Try to import and run the module
            try:
                if module_id == "social_api_client":
                    from social_client.social_api_client import main
                elif module_id == "data_processor":
                    from process.data_processor import main
                elif module_id == "profile_aggregator":
                    from process.profile_aggregator import main
                elif module_id == "posts_consolidator":
                    from process.posts_consolidator import main
                elif module_id == "notion_update":
                    from notion.notion_update import main
                elif module_id == "notion_supabase_sync":
                    from notion.notion_supabase_sync import main
                elif module_id == "supabase_uploader":
                    from process.supabase_uploader import main
                else:
                    print(f"❌ Module {module_id} not implemented in CLI yet.")
                    return
                
                main()
                print(f"✅ {module_info['name']} completed successfully!")
                
            except Exception as e:
                print(f"❌ Error running {module_info['name']}: {e}")
                self.logger.error(f"Module execution failed: {e}")
                
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def show_module_dependencies(self):
        """Display module dependencies in a tree structure."""
        print("\n📋 MODULE DEPENDENCIES")
        print("=" * 40)
        
        for module_id, module_info in self.available_modules.items():
            print(f"\n📁 {module_info['name']} ({module_id})")
            if module_info['dependencies']:
                print("  Dependencies:")
                for dep in module_info['dependencies']:
                    if dep in self.available_modules:
                        dep_name = self.available_modules[dep]['name']
                        print(f"    └── {dep_name} ({dep})")
                    else:
                        print(f"    └── {dep} (external)")
            else:
                print("  No dependencies")
        
        input("\nPress Enter to continue...")
    
    def run_specific_workflow(self):
        """Run a predefined workflow."""
        print("\n🎯 RUN SPECIFIC WORKFLOW")
        print("=" * 35)
        
        # Use workflows from configuration
        for workflow in WORKFLOWS:
            print(f"  {workflow['id']}. {workflow['name']}")
            print(f"     {workflow['description']}")
            print(f"     Modules: {', '.join(workflow['modules'])}")
            print(f"     Estimated time: {workflow['estimated_time']}")
            print()
        
        try:
            choice = input(f"Select workflow (1-{len(WORKFLOWS)}): ").strip()
            
            if choice in [w['id'] for w in WORKFLOWS]:
                workflow = next(w for w in WORKFLOWS if w['id'] == choice)
                
                print(f"\n🚀 Running workflow: {workflow['name']}")
                print(f"Description: {workflow['description']}")
                print(f"Modules: {', '.join(workflow['modules'])}")
                print(f"Estimated time: {workflow['estimated_time']}")
                
                confirm = input("\nProceed? (y/N): ").strip().lower()
                if confirm != 'y':
                    print("❌ Workflow cancelled.")
                    return
                
                # Execute workflow modules in order
                for module_id in workflow['modules']:
                    if module_id in self.available_modules:
                        module_info = self.available_modules[module_id]
                        print(f"\n⏳ Executing: {module_info['name']}")
                        self._run_module(module_id, module_info)
                    else:
                        print(f"❌ Module {module_id} not found!")
                
                print(f"\n✅ Workflow '{workflow['name']}' completed!")
                
            else:
                print("❌ Invalid workflow selection!")
                
        except KeyboardInterrupt:
            print("\n❌ Operation cancelled by user.")
        
        input("\nPress Enter to continue...")
    
    def show_help(self):
        """Display help information."""
        print("\n❓ HELP & INFORMATION")
        print("=" * 40)
        print("""
This CLI provides an interactive interface to manage your data processing project.

MAIN FEATURES:
• Run the complete default pipeline (API → Notion)
• Execute individual modules selectively
• Analyze project structure and dependencies
• Run predefined workflows
• View module information and dependencies

USAGE TIPS:
• The default pipeline is recommended for most use cases
• Check dependencies before running individual modules
• Use the structure analysis to understand execution order
• Workflows provide common operation combinations

MODULE CATEGORIES:
• Input: Data collection from external sources
• Processing: Data transformation and aggregation
• Output: Data export to external systems
• Sync: Synchronization between systems

For more detailed information, check the README files in each module directory.
        """)
        
        input("Press Enter to continue...")
    
    def run(self):
        """Main CLI loop."""
        while True:
            try:
                self.show_welcome()
                self.show_main_menu()
                
                choice = input("Select an option (1-8): ").strip()
                
                if choice == "1":
                    self.run_default_pipeline()
                elif choice == "2":
                    self.show_all_modules()
                elif choice == "3":
                    self.analyze_project_structure()
                elif choice == "4":
                    self.run_custom_module()
                elif choice == "5":
                    self.show_module_dependencies()
                elif choice == "6":
                    self.run_specific_workflow()
                elif choice == "7":
                    self.show_help()
                elif choice == "8":
                    print("\n👋 Goodbye! Thanks for using the CLI.")
                    break
                else:
                    print("❌ Invalid option! Please select 1-8.")
                    input("Press Enter to continue...")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye! Thanks for using the CLI.")
                break
            except Exception as e:
                print(f"\n❌ Unexpected error: {e}")
                self.logger.error(f"Unexpected error in CLI: {e}")
                input("Press Enter to continue...")

def main():
    """Main entry point for the CLI."""
    cli = DataProcessingCLI()
    cli.run()

if __name__ == "__main__":
    main()