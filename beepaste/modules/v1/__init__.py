from sanic import Blueprint
from sanic_cors import CORS

from beepaste.modules.v1.routes.paste import init_paste_routes
from beepaste.modules.v1.routes.auth import init_auth_routes

# init modules
moduleApiV1 = Blueprint('api/v1', url_prefix='/api/v1')
CORS(moduleApiV1,automatic_options=True)

# init modules routes # TODO improve name
init_paste_routes(moduleApiV1)
init_auth_routes(moduleApiV1)
