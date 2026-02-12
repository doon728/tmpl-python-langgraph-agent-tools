import os
import sys
import importlib.util
from typing import Dict, Any

def load_config(env: str = None) -> Dict[str, Any]:
    """
    Load configuration based on environment.
    """
    # Print additional diagnostic information
    print("Python Executable:", sys.executable)
    print("Python Version:", sys.version)
    print("Full Python Path:", sys.path)
    
    # Attempt to import using multiple methods
    try:
        # Method 1: Direct import
        import yaml
        print("✅ PyYAML imported via direct import")
        return _load_config_impl(env)
    except ImportError:
        try:
            # Method 2: importlib
            yaml_spec = importlib.util.find_spec('yaml')
            if yaml_spec:
                yaml = importlib.util.module_from_spec(yaml_spec)
                yaml_spec.loader.exec_module(yaml)
                print("✅ PyYAML imported via importlib")
                return _load_config_impl(env)
        except Exception as e:
            print(f"❌ Failed to import PyYAML: {e}")
    
    raise ImportError("Could not import PyYAML. Please verify installation.")

def _load_config_impl(env: str = None) -> Dict[str, Any]:
    """
    Internal implementation of config loading.
    """
    import yaml  # We know yaml is available here
    
    if env is None:
        env = os.environ.get('AGENT_ENV', 'dev')
    
    config_path = os.path.join(
        os.path.dirname(__file__), 
        f"{env}.yaml"
    )
    
    try:
        with open(config_path, 'r') as config_file:
            return yaml.safe_load(config_file)
    except FileNotFoundError:
        raise ConfigurationError(f"Configuration file for {env} not found")
    except yaml.YAMLError as e:
        raise ConfigurationError(f"Error parsing configuration: {e}")

def get_config(key: str, default=None):
    """
    Retrieve a configuration value, with optional default.
    """
    config = load_config()
    
    # Traverse nested dictionary
    for k in key.split('.'):
        if isinstance(config, dict) and k in config:
            config = config[k]
        else:
            return default
    
    return config
