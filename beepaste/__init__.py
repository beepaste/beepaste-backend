from sanic import Sanic
from beepaste.utils.config import get_config
from beepaste.utils.logger import get_logger
from beepaste.modules import modulePaste, moduleAuth

logger = get_logger('beepaste')

# config
web_cnf = get_config('web_server')
mongo_cnf = get_config('mongodb')
redis_cnf = get_config('redis')

# load sanic application
app = Sanic('beepaste')

# load events after app running
# TODO fix
from beepaste.events import redis  # noqa
from beepaste.events import analytic  # noqa
from beepaste.events import xss  # noqa
from beepaste.events import mongo  # noqa

# add modules
app.blueprint(modulePaste, url_prefix='api/v1/paste')
app.blueprint(moduleAuth, url_prefix='api/v1/auth')
