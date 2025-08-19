#!/usr/bin/env python
"""
Test script for the CLI
Verifies that the CLI can be imported and basic functionality works
"""

import sys
from pathlib import Path

# Add the parent directory to the Python path
sys.path.append(str(Path(__file__).parent.parent))

def test_imports():
    """Test that all required modules can be imported."""
    print("🧪 Testing CLI imports...")
    
    try:
        from cli.config import MODULES, WORKFLOWS, EXECUTION_PLANS, CATEGORIES
        print("✅ Configuration imports successful")
        
        from cli.main import DataProcessingCLI
        print("✅ Main CLI class import successful")
        
        return True
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False

def test_configuration():
    """Test that configuration is properly loaded."""
    print("\n🔧 Testing configuration...")
    
    try:
        from cli.config import MODULES, WORKFLOWS, EXECUTION_PLANS, CATEGORIES
        
        print(f"✅ Found {len(MODULES)} modules")
        print(f"✅ Found {len(WORKFLOWS)} workflows")
        print(f"✅ Found {len(EXECUTION_PLANS)} execution plans")
        print(f"✅ Found {len(CATEGORIES)} categories")
        
        # Check that required modules exist
        required_modules = ["social_api_client", "data_processor", "notion_update"]
        for module in required_modules:
            if module in MODULES:
                print(f"✅ Required module '{module}' found")
            else:
                print(f"❌ Required module '{module}' missing")
                return False
        
        return True
    except Exception as e:
        print(f"❌ Configuration test failed: {e}")
        return False

def test_cli_initialization():
    """Test that CLI can be initialized."""
    print("\n🚀 Testing CLI initialization...")
    
    try:
        from cli.main import DataProcessingCLI
        
        cli = DataProcessingCLI()
        print("✅ CLI instance created successfully")
        
        # Check that modules are loaded
        if hasattr(cli, 'available_modules') and cli.available_modules:
            print(f"✅ {len(cli.available_modules)} modules loaded")
        else:
            print("❌ No modules loaded")
            return False
        
        return True
    except Exception as e:
        print(f"❌ CLI initialization failed: {e}")
        return False

def main():
    """Run all tests."""
    print("🧪 CLI Test Suite")
    print("=" * 40)
    
    tests = [
        test_imports,
        test_configuration,
        test_cli_initialization
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                print(f"❌ Test {test.__name__} failed")
        except Exception as e:
            print(f"❌ Test {test.__name__} crashed: {e}")
    
    print("\n" + "=" * 40)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! CLI is ready to use.")
        return True
    else:
        print("❌ Some tests failed. Please check the errors above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)