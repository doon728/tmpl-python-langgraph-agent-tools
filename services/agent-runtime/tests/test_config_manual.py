import sys
import os

print("Current Working Directory:", os.getcwd())
print("Python Path:", sys.path)

try:
    import yaml
    print("PyYAML successfully imported")
except ImportError as e:
    print(f"PyYAML import error: {e}")

from config.settings import load_config, get_config

def test_manual_config_loading():
    # Load default configuration
    config = load_config()
    print("Full Configuration:", config)

    # Test specific config retrievals
    print("Tool Gateway URL:", get_config('tool_gateway.url'))
    print("Environment:", get_config('environment'))

# This allows running the script directly
if __name__ == '__main__':
    test_manual_config_loading()
