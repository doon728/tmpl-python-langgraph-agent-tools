import os
import sys
import importlib.util

# Add parent directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print("Current Working Directory:", os.getcwd())
print("Python Path:", sys.path)

# Comprehensive yaml import diagnostics
try:
    import yaml
    print("✅ PyYAML imported successfully")
    print("PyYAML version:", yaml.__version__)
    print("PyYAML file location:", yaml.__file__)
except ImportError as e:
    print(f"❌ YAML Import Error: {e}")
    
    # Additional import diagnostics
    try:
        spec = importlib.util.find_spec('yaml')
        print("PyYAML spec:", spec)
    except Exception as import_error:
        print(f"Import spec error: {import_error}")

from config.settings import load_config, get_config

def test_manual_config_loading():
    config = load_config()
    print("Full Configuration:", config)
    print("Tool Gateway URL:", get_config('tool_gateway.url'))
    print("Environment:", get_config('environment'))

if __name__ == '__main__':
    test_manual_config_loading()
