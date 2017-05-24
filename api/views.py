from tools import get_config, get_logger

from sanic.response import json


async def new_paste(request):
    ''' saves a sent JSON object into database and returns a link to it '''

    print(request.json)
    return json({"hello": "world"})
