import os
import yaml
from typing import Dict, Any
from functools import lru_cache

class ConfigurationError(Exception):
    """Raised when configuration cannot be loaded"""
    pass

@lru_cache(maxsize=1)
def load_config(env: str = None) -> Dict[str, Any]:
    """
    Load configuration based on environment.
    
    Args:
        env: Environment name (dev/staging/prod). Defaults to ENV var or 'dev'.
    
    Returns:
        Loaded configuration dictionary
    """
    if env is None:
        env = os.getenv('AGENT_ENV', 'dev')
    
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
    
    Args:
        key: Dot-separated configuration key
        default: Default value if key not found
    
    Returns:
        Configuration value
    """
    config = load_config()
    
    # Traverse nested dictionary
    for k in key.split('.'):
        if isinstance(config, dict) and k in config:
            config = config[k]
        else:
            return default
    
    return config
