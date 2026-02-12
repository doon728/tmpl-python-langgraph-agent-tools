import os
import sys
import yaml

# Add parent directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.settings import load_config, get_config

print("Python Version:", sys.version)
print("Executable:", sys.executable)
print("Current Working Directory:", os.getcwd())
print("Python Path:", sys.path)

# Comprehensive yaml import diagnostics
try:
    print("✅ PyYAML imported successfully")
    print("PyYAML version:", yaml.__version__)
    print("PyYAML file location:", yaml.__file__)
except AttributeError:
    print("✅ PyYAML imported successfully (no version attribute)")

def test_manual_config_loading():
    config = load_config()
    print("Full Configuration:", config)
    print("Tool Gateway URL:", get_config('tool_gateway.url'))
    print("Environment:", get_config('environment'))

if __name__ == '__main__':
    test_manual_config_loading()
