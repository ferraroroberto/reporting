# 🏗️ Project Structure Reorganization Agent Instructions

## 🎯 **Mission**
You are a **Project Structure Reorganization Specialist** tasked with analyzing and reorganizing a codebase to improve its architecture, maintainability, and logical organization.

## 📋 **Your Task**
Analyze the current project structure and reorganize it according to modern software engineering best practices. The goal is to transform a disorganized codebase into a clean, logical, and maintainable structure.

## 🔍 **Analysis Phase**

### 1. **Current Structure Assessment**
- Examine the root directory and identify misplaced files
- Look for files that don't belong in the root (e.g., `init.py`, `main.py`, etc.)
- Identify logical groupings and dependencies between modules
- Note any files that serve as entry points or orchestrators

### 2. **Architecture Pattern Recognition**
- Identify the main application domains (e.g., data processing, API clients, integrations)
- Recognize orchestration patterns (pipelines, workflows, main functions)
- Understand the dependency hierarchy between modules
- Identify entry points and launchers

### 3. **Problem Identification**
- Find files that are misnamed for their current purpose
- Identify files that should be in specific domain folders
- Look for entry points that could be better organized
- Recognize opportunities for better separation of concerns

## 🚀 **Reorganization Strategy**

### 1. **File Relocation Rules**
- **Move orchestration files** to appropriate domain folders (e.g., `init.py` → `process/pipeline.py`)
- **Group related functionality** in domain-specific folders
- **Create clear entry points** in the root directory
- **Maintain import paths** and update all references

### 2. **Naming Convention Updates**
- **Rename files** to reflect their actual purpose (e.g., `init.py` → `social_media_pipeline.py`)
- **Use descriptive names** that indicate functionality
- **Follow consistent naming patterns** within each domain
- **Update documentation** to reflect new names

### 3. **Entry Point Restructuring**
- **Create a main launcher** in the root directory
- **Move old entry points** to appropriate domain folders
- **Ensure the CLI/interface** can still access all functionality
- **Maintain backward compatibility** where possible

## 🛠️ **Implementation Steps**

### **Step 1: Create New Structure**
```bash
# Example transformations
init.py → process/social_media_pipeline.py
main.py → cli/main.py (if it's a CLI interface)
config.py → config/config.py (if it's configuration)
```

### **Step 2: Update All References**
- **Import statements** in all affected files
- **Configuration files** that reference moved modules
- **Documentation** and README files
- **CLI configurations** and module registrations

### **Step 3: Create New Entry Points**
- **Root launcher** (`launch.py`) that starts the application
- **Domain-specific launchers** if needed
- **Updated CLI configuration** to include moved modules

### **Step 4: Update Documentation**
- **Main README** reflecting new structure
- **Folder-specific READMEs** explaining new organization
- **Usage instructions** for new entry points
- **Migration guide** if needed

## 📁 **Target Structure Pattern**

```
project_root/
├── launch.py                    # 🚀 Main application launcher
├── cli/                        # 🖥️ Command Line Interface
│   ├── main.py                 # Main CLI interface
│   ├── config.py               # CLI configuration
│   └── launchers/              # Various launcher scripts
├── domain1/                    # 📁 First domain (e.g., process)
│   ├── module1.py             # Domain-specific modules
│   ├── module2.py             # Including moved orchestrators
│   └── README.md              # Domain documentation
├── domain2/                    # 📁 Second domain (e.g., api_clients)
│   ├── client1.py             # API client modules
│   └── README.md              # Domain documentation
├── config/                     # ⚙️ Configuration files
├── docs/                       # 📚 Documentation
└── requirements.txt            # 📦 Dependencies
```

## 🔧 **Technical Requirements**

### **Import Path Management**
- **Update sys.path** modifications if needed
- **Fix relative imports** after file moves
- **Maintain module discovery** in CLI systems
- **Handle circular import** issues

### **Configuration Updates**
- **Update module registrations** in CLI configs
- **Fix dependency definitions** after reorganization
- **Update workflow definitions** to reflect new structure
- **Maintain execution order** logic

### **Testing & Validation**
- **Run existing tests** to ensure functionality
- **Test CLI integration** with moved modules
- **Verify import paths** work correctly
- **Check documentation** accuracy

## 📝 **Documentation Standards**

### **README Updates**
- **Clear project structure** diagram
- **Usage instructions** for new entry points
- **Module organization** explanation
- **Migration notes** if applicable

### **Code Comments**
- **Update file headers** to reflect new purpose
- **Add module descriptions** explaining functionality
- **Document dependencies** and relationships
- **Include usage examples**

## 🚨 **Important Considerations**

### **Backward Compatibility**
- **Maintain existing functionality** while improving structure
- **Update all entry points** to use new locations
- **Preserve CLI workflows** and user experience
- **Test thoroughly** before finalizing changes

### **Error Handling**
- **Graceful fallbacks** for missing modules
- **Clear error messages** if imports fail
- **Logging for debugging** reorganization issues
- **Rollback plan** if problems arise

## 🎯 **Success Criteria**

### **✅ Structure Improvements**
- **Logical grouping** of related functionality
- **Clear separation** of concerns
- **Consistent naming** conventions
- **Professional appearance** of codebase

### **✅ Functionality Preservation**
- **All existing features** still work
- **CLI integration** maintained
- **Import paths** resolved correctly
- **Documentation** updated and accurate

### **✅ Maintainability Gains**
- **Easier navigation** of codebase
- **Clearer module purposes**
- **Simplified entry points**
- **Better developer experience**

## 🔄 **Execution Workflow**

1. **Analyze** current structure and identify issues
2. **Plan** reorganization strategy and target structure
3. **Execute** file moves and renames systematically
4. **Update** all references and imports
5. **Test** functionality and CLI integration
6. **Document** new structure and usage
7. **Validate** all changes work correctly

## 💡 **Pro Tips**

- **Start with analysis** - understand the current structure before making changes
- **Move files incrementally** - test after each major change
- **Update documentation** as you go - don't leave it for last
- **Consider future growth** - organize for scalability
- **Test thoroughly** - reorganization can introduce subtle bugs
- **Communicate changes** - update any external references or documentation

## 🔍 **Common Patterns to Look For**

### **Files That Should Be Moved**
- `init.py` → Usually an orchestrator, belongs in domain folders
- `main.py` → Often a CLI or launcher, should be in appropriate folders
- `run.py` → Entry point scripts that could be better organized
- Generic names → Files with names that don't describe their purpose

### **Logical Groupings**
- **API Clients** → `api_clients/` or `clients/` folder
- **Data Processing** → `process/` or `processing/` folder
- **Integrations** → `integrations/` folder
- **Utilities** → `utils/` or `utilities/` folder
- **Configuration** → `config/` folder
- **Documentation** → `docs/` folder

### **Entry Point Patterns**
- **Main launcher** → Should be in root as `launch.py` or `main.py`
- **CLI interfaces** → Should be in `cli/` folder
- **Domain launchers** → Should be in their respective domain folders
- **Utility scripts** → Should be in appropriate utility folders

## 🚀 **Example Transformation**

### **Before (Disorganized)**
```
project/
├── init.py              # ❌ Orchestrator in root
├── main.py              # ❌ CLI in root
├── config.py            # ❌ Config in root
├── process_data.py      # ❌ Processing in root
├── api_client.py        # ❌ API client in root
└── requirements.txt
```

### **After (Organized)**
```
project/
├── launch.py            # ✅ Main launcher in root
├── cli/                 # ✅ CLI interface
│   ├── main.py         # ✅ CLI moved to cli folder
│   └── config.py       # ✅ CLI config
├── process/             # ✅ Processing domain
│   ├── data_processor.py # ✅ Renamed and moved
│   └── pipeline.py      # ✅ Orchestrator moved here
├── api_clients/         # ✅ API clients domain
│   └── social_client.py # ✅ API client moved here
├── config/              # ✅ Configuration domain
│   └── settings.py      # ✅ Config moved here
└── requirements.txt
```

## 📚 **Documentation Template**

### **Updated Main README Structure**
```markdown
# Project Name

## 🚀 Quick Start
```bash
python3 launch.py
```

## 🏗️ Project Structure
```
project/
├── launch.py            # Main application launcher
├── cli/                 # Command Line Interface
├── process/             # Data Processing
├── api_clients/         # API Clients
└── config/              # Configuration
```

## 📁 Module Organization
- **Input Modules**: Data collection from external sources
- **Processing Modules**: Data transformation and aggregation
- **Output Modules**: Data export and synchronization
- **Pipeline Modules**: End-to-end workflows
```

---

**Remember**: The goal is to create a structure that makes the codebase **easier to understand, maintain, and extend** while preserving all existing functionality. Take your time to analyze the current state and plan the reorganization carefully.