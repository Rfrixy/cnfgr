import os
config = {}


def initialize():
    files = ['config', 'private_config']
    for file in files:
        try:
            file_object = __import__(file)
            config.update({k: v for k, v in vars(file_object).items() if not k.startswith('_')})
        except ImportError:
            pass


def set(key, value):
    config[key] = value


def get(key):
    return config[key]


initialize()
