from beepaste import app, jwt_cnf, limits_cnf
import jwt
from jwt.exceptions import (DecodeError, ExpiredSignatureError)
from sanic import response
from beepaste.redis import redis


@app.middleware('request')
async def checkAuth(request):
    if request.headers.get('X-TOKEN'):
        encoded = request.headers['X-TOKEN']
        try:
            decodedtoken = jwt.decode(encoded, jwt_cnf['secret'],
                                     algorithm=jwt_cnf['algorithm'])

            if decodedtoken['userid'] == 0:
                source_string = decodedtoken['ip'] + '_limits'
            else:
                source_string = decodedtoken['userid'] + '_limits'

            token_stat = await redis.get_value(encoded + '_stat')

            if token_stat != b'valid':
                return response.json(
                    {'status': 'fail', 'details': 'invalid token'},
                    status=403)

            token_limits_exists = await redis.exists(encoded + '_limits')
            source_limits_exists = await redis.exists(source_string)

            if not token_limits_exists:
                await redis.set_dict(encoded + '_limits', limits_cnf)
                await redis.expire(encoded + '_limits', limits_cnf['reset_timeout'])

            if not source_limits_exists:
                await redis.set_dict(source_string, limits_cnf)
                await redis.expire(source_string, limits_cnf['reset_timeout'])

            token_limits = await redis.get_dict(encoded + '_limits')
            source_limits = await redis.get_dict(source_string)

            request['token_limits'] = token_limits
            request['source_limits'] = source_limits

            request['userid'] = decodedtoken['userid']

        except DecodeError as e:
            return response.json(
                {'status': 'fail', 'details': 'invalid token'},
                status=400)
        except ExpiredSignatureError as e:
            return response.json(
                {'status': 'fail', 'details': 'token expired'},
                status=400)
    else:
        request['userid'] = None

@app.middleware('response')
async def setAuth(request, response):
    if 'userid' in request and request.headers.get('X-TOKEN'):
        encoded = request.headers['X-TOKEN']
        decodedtoken = jwt.decode(encoded, jwt_cnf['secret'],
                                 algorithm=jwt_cnf['algorithm'])

        if decodedtoken['userid'] == 0:
            source_string = decodedtoken['ip'] + '_limits'
        else:
            source_string = decodedtoken['userid'] + '_limits'

        await redis.set_dict(encoded + '_limits', request['token_limits'])
        await redis.set_dict(source_string, request['source_limits'])
