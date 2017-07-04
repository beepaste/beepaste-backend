from sanic import Sanic
from beepaste.utils.config import get_config
from beepaste.utils.logger import lg

# config
# TODO all config to some variable like setting or somthing like that
# available of request !
web_cnf = get_config('app')
mongo_cnf = get_config('mongodb')
redis_cnf = get_config('redis')
jwt_cnf = get_config('jwt')
limits_cnf = get_config('limits')
# lg(1, 'config loaded')

# load sanic application
app = Sanic('beepaste')

# load events after app running
# TODO fix use somthing like after server start
from beepaste.modules import *  # noqa
from beepaste.events import auth  # noqa
from beepaste.events import xss  # noqa
from beepaste.events import mongo  # noqa

# add modules
app.blueprint(moduleApiV1, url_prefix='api/v1')
