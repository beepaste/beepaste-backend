import yaml
import os


def get_config(section):
    dirname = os.path.dirname
    try:
        conf_file = dirname(os.path.realpath(__file__)) + '/config.yaml'
        with open(conf_file, 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
    except FileNotFoundError:
        return {}
    try:
        return cfg[section]
    except KeyError:
        return {}


def get_logger(logger_name=''):
    import logging
    from logging.config import dictConfig
    logging_config = get_config('logger')
    dictConfig(logging_config)
    logger = logging.getLogger(logger_name)
    return logger
