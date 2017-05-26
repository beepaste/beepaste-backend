from tools import get_config, get_logger
from models import paste
from sanic.response import json


async def new_paste(request):
    ''' saves a sent JSON object into database and returns a link to it '''
    input_json = request.json
    new_paste = Paste(**input_json)
    # TODO: write saving to db and get the link
    return json({"hello": "world"})
