import os
import sys

# Add parent directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print("Python Path:", sys.path)
print("Poetry Virtual Environment:", os.environ.get('POETRY_ACTIVE'))

# Attempt to install packages directly
try:
    import subprocess
    result = subprocess.run(['poetry', 'add', 'pyyaml', 'setuptools'], capture_output=True, text=True)
    print("Poetry install output:", result.stdout)
    print("Poetry install errors:", result.stderr)
except Exception as e:
    print(f"Could not run poetry add: {e}")

# Now try importing
try:
    import yaml  # noqa: F401
    print("PyYAML successfully imported")
except ImportError as e:
    print(f"YAML Import Error: {e}")

from config.settings import load_config, get_config

def test_manual_config_loading():
    config = load_config()
    print("Full Configuration:", config)
    print("Tool Gateway URL:", get_config('tool_gateway.url'))
    print("Environment:", get_config('environment'))

if __name__ == '__main__':
    test_manual_config_loading()
