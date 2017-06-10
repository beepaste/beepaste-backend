import os
import yaml


def get_config(section):
    try:
        # TODO must impl cli script to load dev and pro separately
        conf_file = os.path.dirname('..') + 'config/config-dev.yaml'
        with open(conf_file, 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
    except FileNotFoundError:
        return {}
    try:
        return cfg[section]
    except KeyError:
        return {}
