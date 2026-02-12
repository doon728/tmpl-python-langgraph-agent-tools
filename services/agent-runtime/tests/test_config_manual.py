import os
import sys
import yaml  # Import at the top
from config.settings import load_config, get_config

# Add parent directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print("Python Executable:", sys.executable)
print("Python Version:", sys.version)
print("Current Working Directory:", os.getcwd())
print("Python Path:", sys.path)

def test_manual_config_loading():
    config = load_config()
    print("Full Configuration:", config)
    # Adjust these based on your actual configuration structure
    print("Tool Gateway URL:", get_config('tool_gateway.url'))
    print("Environment:", get_config('environment'))

if __name__ == '__main__':
    test_manual_config_loading()
