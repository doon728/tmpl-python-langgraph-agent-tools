import os
import sys
import importlib.util

# Add parent directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Explicitly try to import yaml
try:
    import yaml
except ImportError:
    # Diagnostic information
    print("Python Path:", sys.path)
    spec = importlib.util.find_spec('yaml')
    print("PyYAML spec:", spec)
    raise

from config.settings import load_config, get_config

print("Current Working Directory:", os.getcwd())
print("Python Path:", sys.path)

# Comprehensive yaml import diagnostics
def check_yaml_import():
    try:
        print("✅ PyYAML imported successfully")
        print("PyYAML version:", yaml.__version__)
        print("PyYAML file location:", yaml.__file__)
        return True
    except AttributeError:
        # Some versions of PyYAML might not have __version__
        print("✅ PyYAML imported successfully (no version attribute)")
        return True
    except ImportError as e:
        print(f"❌ YAML Import Error: {e}")
        return False

# Verify yaml import
yaml_available = check_yaml_import()

def test_manual_config_loading():
    config = load_config()
    print("Full Configuration:", config)
    print("Tool Gateway URL:", get_config('tool_gateway.url'))
    print("Environment:", get_config('environment'))

if __name__ == '__main__':
    test_manual_config_loading()
