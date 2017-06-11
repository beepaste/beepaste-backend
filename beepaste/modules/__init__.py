from sanic import Blueprint
from beepaste.modules.paste.routes import init_paste_routes
from beepaste.modules.auth.routes import init_auth_routes
from beepaste.modules.stat.routes import init_stat_routes
from beepaste.modules.doc.routes import init_doc_routes

# init modules
modulePaste = Blueprint('api/v1/paste', url_prefix='/api/v1/paste')
moduleAuth = Blueprint('api/v1/auth', url_prefix= '/api/v1/auth')
moduleStat = Blueprint('api/v1/stat', url_prefix= '/api/v1/stat')
moduleDoc = Blueprint('api/v1', url_prefix= '/api/v1')

# init modules routes # TODO improve name
init_paste_routes(modulePaste)
init_auth_routes(moduleAuth)
init_stat_routes(moduleStat)
init_doc_routes(moduleDoc)
