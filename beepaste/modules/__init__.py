from sanic import Blueprint
from beepaste.modules.v1.routes.paste import init_paste_routes
from beepaste.modules.v1.routes.auth import init_auth_routes

# init modules
modulePaste = Blueprint('api/v1/paste', url_prefix='/api/v1/paste')
moduleAuth = Blueprint('api/v1/auth', url_prefix='/api/v1/auth')

# init modules routes # TODO improve name
init_paste_routes(modulePaste)
init_auth_routes(moduleAuth)
