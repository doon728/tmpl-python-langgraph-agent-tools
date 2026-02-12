import os
import importlib.util
from typing import Dict, Any

def load_config(env: str = None) -> Dict[str, Any]:
    """
    Load configuration based on environment.
    """
    # Explicitly try to import yaml
    try:
        import yaml
    except ImportError:
        # Print detailed diagnostic information
        print("Import Diagnostic Information:")
        print("Python Path:", os.sys.path)
        print("Attempting to locate yaml via importlib:")
        yaml_spec = importlib.util.find_spec('yaml')
        print("PyYAML spec:", yaml_spec)
        
        raise ImportError("Could not import PyYAML. Please verify installation.")
    
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
