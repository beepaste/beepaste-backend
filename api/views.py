from tools import get_config, get_logger
from models.paste import Paste
from sanic.response import json
from models.api import Api
import datetime


async def new_paste(request): # POST request
    ''' saves a sent JSON object into database and returns a link to it '''
    mongo_config = get_config('mongodb')
    mongo_db = MongoDB(mongo_config)
    input_json = request.json
    new_paste = Paste(**input_json)
    #res = mongo_db.insert(new_paste)
    new_paste.save(mongo_db)
    # TODO: write saving to db and get the link
    return json({"hello": "world"})

async def new_api_token(request): # GET request
    ''' generates new api-key if it was ok (no more than 5 tokens in 15minutes) '''
    new_api = Api(expires=(datetime.datetime.utcnow() + datetime.timedelta(minutes=15)).timestamp(),
                  ownerID=0, ip_address=request.ip)
    mongo_config = get_config('mongodb')
    dbEngine = MongoDB(mongo_config)
    time_delta = await new_api.countInTime(dbEngine, datetime.datetime.utcnow() - datetime.timedelta(minutes=15))
    if time_delta < 5:
        new_api.genSecret()
        new_api.genToken()
        if new_api.is_valid:
            new_api.save()
            return json({'state': 'success', 'token': new_api['token']})
    return json({'stat': 'received'})
