import os
import sys
import importlib.util

# Add parent directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Comprehensive system and import diagnostics
print("Python Executable:", sys.executable)
print("Python Version:", sys.version)
print("Current Working Directory:", os.getcwd())
print("Python Path:", sys.path)

# Detailed YAML import diagnostic
def diagnose_yaml_import():
    try:
        # Method 1: Standard import
        import yaml
        print("✅ PyYAML imported successfully (standard)")
        print("PyYAML version:", yaml.__version__)
        print("PyYAML file location:", yaml.__file__)
        return yaml
    except ImportError:
        print("❌ Standard import failed")
        
        # Method 2: importlib import
        try:
            spec = importlib.util.find_spec('yaml')
            if spec is not None:
                print("PyYAML spec found:", spec)
                yaml = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(yaml)
                print("✅ PyYAML imported via importlib")
                return yaml
            else:
                print("❌ No PyYAML spec found")
        except Exception as e:
            print(f"❌ Importlib method failed: {e}")
    
    return None

# Attempt to import yaml
yaml = diagnose_yaml_import()

from config.settings import load_config, get_config

def test_manual_config_loading():
    config = load_config()
    print("Full Configuration:", config)
    print("Tool Gateway URL:", get_config('tool_gateway.url'))
    print("Environment:", get_config('environment'))

if __name__ == '__main__':
    test_manual_config_loading()
