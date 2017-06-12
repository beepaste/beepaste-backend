from .config import get_config


def get_logger(logger_name=''):
    import logging
    from logging.config import dictConfig
    logging_config = get_config('logger')
    dictConfig(logging_config)
    logger = logging.getLogger(logger_name)
    return logger


logger = get_logger('beepaste')
