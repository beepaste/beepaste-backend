from sanic import Blueprint
from beepaste.modules.apiv1.routes import add_api_routes

# init modules
moduleApiV1 = Blueprint('api/v1', url_prefix='/api/v1')
# init modules routes # TODO improve name
add_api_routes(moduleApiV1)
