from sanic import Sanic, response
from beepaste.utils.config import get_config
from beepaste.utils.logger import lg

# config
# TODO all config to some variable like setting or somthing like that
# available of request !
global_cnf = get_config('global')
web_cnf = get_config('app')
mongo_cnf = get_config('mongodb')
redis_cnf = get_config('redis')
jwt_cnf = get_config('jwt')
limits_cnf = get_config('limits')
bitly_cnf = get_config('bitly')
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

# Exception Handling!
from sanic.exceptions import NotFound
from sanic.exceptions import ServerError

@app.exception(NotFound)
def reponse404(request, exception):
    return response.json({'status': 'fail', 'details': "Route Not found"}, status=404)

@app.exception(ServerError)
def reponse500(request, exception):
    print(exception)
    return response.json({'status': 'fail', 'details': "Some error occured"}, status=500)
