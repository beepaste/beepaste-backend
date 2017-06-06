import yaml
from sanic import Sanic
from sanic.response import json
from asymongo import connect

from api import views, tools
from tools import get_config, get_logger

# logger = get_logger()
web_cnf = get_config('web_server')
mongo_cnf = get_config('mongodb')

# making connection to mongodb
connect(**mongo_cnf)

# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
app = Sanic()

tools.add_api_routes(app)

if __name__ == "__main__":
    # logger.info('Starting server')
    app.run(**web_cnf)
