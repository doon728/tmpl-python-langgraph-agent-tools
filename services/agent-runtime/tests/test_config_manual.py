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
