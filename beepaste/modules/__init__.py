from sanic import Blueprint
from beepaste.modules.paste.routes import init_paste_routes
from beepaste.modules.auth.routes import init_auth_routes

# init modules
modulePaste = Blueprint('api/v1/paste', url_prefix='/api/v1/paste')
moduleAuth = Blueprint('api/v1/auth', url_prefix= '/api/v1/auth')

# init modules routes # TODO improve name
init_paste_routes(modulePaste)
init_auth_routes(moduleAuth)
