import datetime
import json

import sanic.response as resp
from beepaste import logger
from beepaste.events import redis
from beepaste.utils.config import get_config
from mongoengine.errors import ValidationError

from .api import Api
from .paste import Paste

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
        return resp.json(
            {'status': 'success', 'paste': new_paste_obj},
            ,status=201)
    except ValidationError as e:
        print(e)
        return resp.json(
                {'status': 'fail', 'details': 'invalid data'},
                status=400)
    except Exception as e:
        print(e)
        return resp.json(
                {'status': 'fail', 'details': 'server error'},
                status=500)


async def new_api_token(request):
    try:
        limits = get_config('limits')
    except Exception:
        logger.critical('config file not found.. aborting')
        return resp.json(
            {'status': 'fail', 'details': 'server error'},
            status=500)
    try:
        all_keys = await redis.redis.connection.mget_aslist(request.ip)
        if len(all_keys) < limits.get(token_for_ip):
            new_api = Api()
            new_api.genSecret()
            new_api.genToken()
            await redis.redis.connection.set(request.ip, new_api.token)
            redis.redis.connection.expire(request.ip, limits.get(reset_timeout))
            new_api.save()
        else:
            logger.info('too many connections for ip{}'.format(request.ip))
            return resp.json(
                {'status': 'fail', 'details': 'too many connections'},
                status=201)
    except Exception:
        logger.critical('connection to Redis failed')
        return resp.json(
            {'status': 'fail', 'details': 'server error'},
            status=500)
    # TODO move to another modules
    '''
    generates new api-key if it was ok
    (no more than 5 tokens in 15minutes)
    '''
    return resp.json({'stat': 'received'})
