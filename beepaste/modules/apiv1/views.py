from beepaste.utils.config import get_config
from .paste import Paste
from .api import Api
from sanic.response import json
import datetime


async def get_paste(request):
    return json({"hello": "world"})


async def post_paste(request):
    ''' saves a sent JSON object into database and returns a link to it '''
    # input_json = request.json
    # new_paste = Paste(**input_json)
    # new_paste.save()
    # TODO: write saving to db and get the link
    return json({"hello": "world"})



async def new_api_token(request):
    # TODO move to another modules
    ''' 
    generates new api-key if it was ok
    (no more than 5 tokens in 15minutes)
    '''

    new_api = Api(expires=(
        datetime.datetime.utcnow() + datetime.timedelta(
            minutes=15)).timestamp(), ownerID=0, ip_address=request.ip)
    mongo_config = get_config('mongodb')
    dbEngine = MongoDB(mongo_config)
    time_delta = await new_api.countInTime(
            dbEngine,
            datetime.datetime.utcnow() - datetime.timedelta(minutes=15)
            )
    if time_delta < 5:
        new_api.genSecret()
        new_api.genToken()
        if new_api.is_valid:
            new_api.save()
            return json({'state': 'success', 'token': new_api['token']})
    return json({'stat': 'received'})
