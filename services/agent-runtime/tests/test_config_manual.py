import os
import sys

# Explicitly modify Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Diagnostic import
try:
    import yaml
except ImportError:
    print("Failed to import yaml. Debugging information:")
    print("Python Path:", sys.path)
    raise

from config.settings import load_config, get_config

def test_manual_config_loading():
    config = load_config()
    print("Full Configuration:", config)
    print("Tool Gateway URL:", get_config('tool_gateway.url'))
    print("Environment:", get_config('environment'))

if __name__ == '__main__':
    test_manual_config_loading()
