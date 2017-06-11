from beepaste.utils.config import get_config
from .paste import Paste
from .api import Api
import sanic.response as resp
import datetime
from mongoengine.errors import ValidationError
import json
from sanic.response import text


async def get_paste(request):
    counter = request['session']['counter']
    path = request['session']['path']
    ip = request['session']['ip']
    return resp.json({
                "hello": "world",
                "counter": counter,
                "ip": ip,
                "path": path
                })

async def post_paste(request):
    ''' saves a sent JSON object into database and returns a link to it '''
    input_json = request.json
    # TODO validation with some lib like marshmallow
    # https://github.com/marshmallow-code/marshmallow
    # not use try catch if validate faild return error from marshmallow 
    # else pass to the model 
    new_paste = Paste(**input_json)
    try:
        # TODO: set ownerID using the token used to authorize api!
        new_paste.views = 0
        await new_paste.generate_url()
        new_paste.validate()
        new_paste.save()
        new_paste_obj = json.loads(new_paste.to_json())
        ret_data = {
            'status': 'success',
            'paste': new_paste_obj
        }
        return resp.json(ret_data)
    except ValidationError as e:
        print(e)
        return json.loads(
                {'status': 'fail', 'details': 'invalid data'}, 
                status=400)
    except Exception as e:
        print(e)
        return json.loads(
                {'status': 'fail', 'details': 'server error'},
                status=500)

async def new_api_token(request):
    # TODO move to another modules
    '''
    generates new api-key if it was ok
    (no more than 5 tokens in 15minutes)
    '''
    return json.loads({'stat': 'received'})
