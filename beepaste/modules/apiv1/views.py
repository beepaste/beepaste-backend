from beepaste.utils.config import get_config
from .paste import Paste
from .api import Api
from sanic.response import json
import datetime
from mongoengine.errors import ValidationError
from pyshorteners import Shortener
from beepaste.utils.config import get_config
import string
from random import *
import asyncio
import uvloop

async def get_paste(request):
    return json({"hello": "world"})


async def post_paste(request):
    ''' saves a sent JSON object into database and returns a link to it '''
    input_json = request.json
    new_paste = Paste(**input_json)
    try:
        # TODO: set ownerID using the token used to authorize api!
        new_paste.views = 0
        await new_paste.generate_url()
        new_paste.validate()
        new_paste.save()
        return json({'status': 'success', 'paste': new_paste.to_mongo()})
    except ValidationError as e:
        print(e)
        return json({'status': 'fail', 'details': 'invalid data'}, status=400)
#    except:
#        return json({'status': 'fail', 'details': 'server error'}, status=500)

async def new_api_token(request):
    # TODO move to another modules
    '''
    generates new api-key if it was ok
    (no more than 5 tokens in 15minutes)
    '''
    return json({'stat': 'received'})
