import os
import sys

# Diagnostic import check
try:
    import yaml  # noqa: F401
    print("PyYAML successfully imported")
except ImportError as e:
    print(f"YAML Import Error: {e}")
    print("Python Path:", sys.path)
    import pkg_resources
    try:
        print("Installed packages:", pkg_resources.working_set)
    except Exception as pkg_err:
        print(f"Could not list packages: {pkg_err}")

from config.settings import load_config, get_config

print("Current Working Directory:", os.getcwd())
print("Python Path:", sys.path)

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
