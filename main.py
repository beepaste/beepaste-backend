import yaml
from sanic import Sanic
from sanic.response import json
from SanicMongo import connect

from api import views, tools
from tools import get_config, get_logger

logger = get_logger('beepaste')

web_cnf = get_config('web_server')
mongo_cnf = get_config('mongodb')

# making connection to mongodb
logger.info('initiating connection to mongodb using config')
connect(**mongo_cnf)
logger.info('connected to mongodb')

# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
app = Sanic()

tools.add_api_routes(app)

if __name__ == "__main__":
    logger.info('Starting server')
    app.run(**web_cnf)
