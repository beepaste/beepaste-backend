from .config import get_config
import asyncio
import logging
from pygelf import GelfTcpHandler, GelfHttpHandler
from logging.config import dictConfig

logg = None

def get_logger(logger_name=''):
    logging_config = get_config('logger')
    dictConfig(logging_config)
    logger = logging.getLogger(logger_name)
    return logger

def sendToLog(lvl, msg):
    global logg
    if logg is None:
        logg = get_logger('beepaste')
    # logg.log(lvl, msg)
    if lvl == 'INFO':
        logg.info(msg)
    elif lvl == 'DEBUG':
        logg.debug(msg)
    elif lvl == 'WARNING':
        logg.warning(msg)
    elif lvl == 'CRITICAL':
        logg.critical(msg)
    elif lvl == 'ERROR':
        logg.error(msg)

async def lg(lvl, msg):
    sendToLog(lvl, msg)
    #loop = asyncio.get_event_loop()
    #await loop.run_in_executor(None, sendToLog, lvl, msg)
