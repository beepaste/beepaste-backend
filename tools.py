import os


def get_config(section):
    dirname = os.path.dirname
    try:
        conf_file = dirname(os.path.realpath(__file__)) + '/confi2g.yaml'
        with open(conf_file, 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
    except FileNotFoundError:
        #TODO: Log this
        return {}
    try:
        return cfg[section]
    except KeyError:
        #TODO: Log this
        return {}


def get_logger():
    import logging
    from logging.config import dictConfig
    logging_config = get_config('logger')
    dictConfig(logging_config)
    logger = logging.getLogger()
    return logger
