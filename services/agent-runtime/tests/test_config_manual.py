import os
import sys

# Add parent directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print("Python Executable:", sys.executable)
print("Python Version:", sys.version)
print("Current Working Directory:", os.getcwd())
print("Python Path:", sys.path)

# Check installed packages
try:
    import pkg_resources
    installed_packages = [d for d in pkg_resources.working_set]
    print("Installed Packages:", [str(p) for p in installed_packages])
except ImportError:
    print("Could not import pkg_resources")

# Try importing yaml
try:
    import yaml
    print("✅ PyYAML imported successfully")
except ImportError as e:
    print(f"❌ YAML Import Error: {e}")

from config.settings import load_config, get_config

def test_manual_config_loading():
    config = load_config()
    print("Full Configuration:", config)
    print("Tool Gateway URL:", get_config('tool_gateway.url'))
    print("Environment:", get_config('environment'))

if __name__ == '__main__':
    test_manual_config_loading()
