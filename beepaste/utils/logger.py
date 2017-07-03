from .config import get_config
import asyncio


def get_logger(logger_name=''):
    import logging
    from logging.config import dictConfig
    logging_config = get_config('logger')
    dictConfig(logging_config)
    logger = logging.getLogger(logger_name)
    return logger


async def lg(lvl, message):
    logger = get_logger('beepaste')
    loop = asyncio.get_event_loop()
    level = {1: 'INFO',
             2: 'DEBUG',
             3: 'WARNING',
             4: 'ERROR',
             5: 'CRITICAL'}
    await loop.run_in_executor(None, logger.log, level.get('level', 'ERROR'), message)
