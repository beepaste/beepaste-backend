from sanic import Sanic
from SanicMongo import connect
from beepaste.utils.config import get_config
from beepaste.utils.logger import get_logger
from beepaste.modules import moduleApiV1

logger = get_logger('beepaste')

# config
web_cnf = get_config('web_server')
mongo_cnf = get_config('mongodb')

# db init
logger.info('initiating connection to mongodb using config')
connect(**mongo_cnf)
logger.info('connected to mongodb')


def app():
    # load sanic application
    app = Sanic('beepaste')

    # add modules
    app.blueprint(moduleApiV1, url_prefix='api/v1')

    return app
