from beepaste import app
import jwt


@app.middleware('request')
async def checkAuth(request):
    if request.headers.get('X-TOKEN'):
        encoded = request.headers['X-TOKEN']
        decodetoken = jwt.decode(encoded, 'secret', algorithms=['HS256'])
        # TODO check if token not decoded or validate some response to user
        request['userid'] = decodetoken['userid']
    else:
        request['userid'] = None
