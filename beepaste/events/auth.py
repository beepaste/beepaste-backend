from beepaste import app, jwt_cnf
import jwt


@app.middleware('request')
async def checkAuth(request):
    if request.headers.get('X-TOKEN'):
        encoded = request.headers['X-TOKEN']
        decodetoken = jwt.decode(encoded, jwt_cnf['secret'],
                                 algorithm=jwt_cnf['algorithm'])
        # TODO check if token not decoded or validate some response to user
        request['userid'] = decodetoken['userid']
    else:
        request['userid'] = None
