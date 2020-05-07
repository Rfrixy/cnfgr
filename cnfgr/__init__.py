import sys
import os
sys.path.append(os.path.abspath(''))

config = {}


def update_config(file_name):
    try:
        file_object = __import__(file_name)
        config.update({k: v for k, v in vars(
            file_object).items() if not k.startswith('_')})
    except ImportError:
        pass


def update_deep(path, value):
    keys = path.split('__')
    d = config
    for key in keys[1:-1]:  # remove 'cfngr.' from the start
        if key not in d:
            d[key] = {}
        if not isinstance(d[key], dict):
            print(type(d[key]))
            raise ValueError('Failed to add key: ' + path + ' at: ' + key +
                             ' - Non-dictionary values already present')
        d = d[key]
    d[keys[-1]] = value


def update_config_with_env():
    config_env_vars = {k: v for k,
                       v in os.environ.items() if k.startswith('CNFGR__')}
    for k, v in config_env_vars.items():
        update_deep(k, v)


def initialize():
    update_config('config')
    update_config_with_env()
    update_config('private_config')
    print(config)


def set(key, value):
    config[key] = value


def get(key):
    return config[key]


initialize()
