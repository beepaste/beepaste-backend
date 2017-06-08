from sanic import Blueprint

from api.v1 import tools as v1_tools

api_v1 = Blueprint('v1', url_prefix='/api/v1')
v1_tools.add_api_routes(api_v1)
