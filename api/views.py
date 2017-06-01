from tools import get_config, get_logger
from models.paste import Paste
from db.mongodb import MongoDB
from sanic.response import json


async def new_paste(request):
    ''' saves a sent JSON object into database and returns a link to it '''
    mongo_config = get_config('mongodb')
    mongo_db = MongoDB(mongo_config)
    input_json = request.json
    new_paste = Paste(**input_json)
    #res = mongo_db.insert(new_paste)
    new_paste.save(mongo_db)
    # TODO: write saving to db and get the link
    return json({"hello": "world"})
