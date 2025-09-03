#!/usr/bin/env python3
"""
Simple test to verify PyYAML functionality after version update.
This test ensures the YAML loading functionality in main.py works correctly.
"""

import yaml
import sys

def test_yaml_basic_functionality():
    """Test basic YAML loading functionality"""
    test_yaml_content = """
    name: "test"
    version: 1.0
    features:
      - security
      - testing
    """
    
    try:
        # Test safe loading (recommended)
        result_safe = yaml.safe_load(test_yaml_content)
        print("✓ yaml.safe_load() works correctly")
        print(f"  Loaded data: {result_safe}")
        
        # Test the loader used in main.py (yaml.Loader)
        # Note: This is intentionally unsafe for demo purposes
        result_unsafe = yaml.load(test_yaml_content, Loader=yaml.Loader)
        print("✓ yaml.load() with yaml.Loader works correctly")
        print(f"  Loaded data: {result_unsafe}")
        
        # Verify both results are equivalent for normal YAML
        if result_safe == result_unsafe:
            print("✓ Both loading methods produce equivalent results for normal YAML")
        else:
            print("⚠ Loading methods produce different results (unexpected)")
            return False
            
        return True
        
    except Exception as e:
        print(f"✗ YAML loading failed: {e}")
        return False

def test_yaml_version():
    """Test that PyYAML version is as expected"""
    try:
        version = yaml.__version__
        print(f"✓ PyYAML version: {version}")
        
        # Check if version is 5.4 or higher (for security fix)
        major, minor = map(int, version.split('.')[:2])
        if major > 5 or (major == 5 and minor >= 4):
            print("✓ PyYAML version meets security requirements (>= 5.4)")
            return True
        else:
            print(f"⚠ PyYAML version {version} is below recommended 5.4")
            return False
            
    except Exception as e:
        print(f"✗ Version check failed: {e}")
        return False

def test_main_app_import():
    """Test that main.py can be imported successfully"""
    try:
        import main
        print("✓ main.py imports successfully")
        
        # Test that the Flask app is created
        if hasattr(main, 'app'):
            print("✓ Flask app is initialized")
        else:
            print("⚠ Flask app not found in main.py")
            return False
            
        return True
        
    except Exception as e:
        print(f"✗ Failed to import main.py: {e}")
        return False

def main():
    """Run all tests"""
    print("Testing PyYAML functionality...")
    print("=" * 50)
    
    tests = [
        test_yaml_version,
        test_yaml_basic_functionality,
        test_main_app_import,
    ]
    
    results = []
    for test in tests:
        print(f"\nRunning {test.__name__}:")
        result = test()
        results.append(result)
        print()
    
    print("=" * 50)
    passed = sum(results)
    total = len(results)
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("✓ All tests passed!")
        return 0
    else:
        print("⚠ Some tests failed!")
        return 1

if __name__ == "__main__":
    sys.exit(main())