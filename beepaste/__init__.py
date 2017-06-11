from sanic import Sanic
from beepaste.utils.config import get_config
from beepaste.utils.logger import get_logger
from beepaste.modules import modulePaste, moduleAuth, moduleStat, moduleDoc

logger = get_logger('beepaste')

# config
# TODO all config to some variable like setting or somthing like that
# available of request !
web_cnf = get_config('app')
mongo_cnf = get_config('mongodb')
redis_cnf = get_config('redis')
jwt_cnf = get_config('jwt')

# load sanic application
app = Sanic('beepaste')

# load events after app running
# TODO fix use somthing like after server start
from beepaste.events import stat  # noqa
from beepaste.events import auth  # noqa
from beepaste.events import analytic  # noqa
from beepaste.events import xss  # noqa
from beepaste.events import mongo  # noqa

# add modules
app.blueprint(modulePaste, url_prefix='api/v1/paste')
app.blueprint(moduleAuth, url_prefix='api/v1/auth')
app.blueprint(moduleStat, url_prefix='api/v1/stat')
app.blueprint(moduleDoc, url_prefix='api/v1')
