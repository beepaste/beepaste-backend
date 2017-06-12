from beepaste import app, jwt_cnf
import jwt
from jwt.exceptions import (DecodeError, ExpiredSignatureError)
from sanic import response


@app.middleware('request')
async def checkAuth(request):
    if request.headers.get('X-TOKEN'):
        encoded = request.headers['X-TOKEN']
        try:
            decodetoken = jwt.decode(encoded, jwt_cnf['secret'],
                                     algorithm=jwt_cnf['algorithm'])
        except DecodeError as e:
            return response.json(
                {'status': 'fail', 'details': 'invalid token'},
                status=400)
        except ExpiredSignatureError as e:
            return response.json(
                {'status': 'fail', 'details': 'token expired'},
                status=400)
        request['userid'] = decodetoken['userid']
    else:
        request['userid'] = None
