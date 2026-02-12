import os
import sys
import subprocess

# Add parent directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print("Python Path:", sys.path)
print("Poetry Virtual Environment:", os.environ.get('POETRY_ACTIVE'))

try:
    import yaml  # noqa: F401
    print("PyYAML successfully imported")
except ImportError as e:
    print(f"YAML Import Error: {e}")
    try:
        result = subprocess.run(['poetry', 'add', 'pyyaml'], capture_output=True, text=True)
        print("Poetry install output:", result.stdout)
        print("Poetry install errors:", result.stderr)
    except Exception as install_error:
        print(f"Could not run poetry add: {install_error}")

from config.settings import load_config, get_config

print("Current Working Directory:", os.getcwd())
print("Python Path:", sys.path)

def test_manual_config_loading():
    config = load_config()
    print("Full Configuration:", config)
    print("Tool Gateway URL:", get_config('tool_gateway.url'))
    print("Environment:", get_config('environment'))

if __name__ == '__main__':
    test_manual_config_loading()
