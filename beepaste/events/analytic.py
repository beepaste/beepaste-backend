from beepaste import app
from random import randint


@app.middleware('request')
async def add_analytic_to_session(request):
    # TODO save some data to session on redis db
    if not request['session'].get('counter'):
        request['session']['counter'] = 0
    request['session']['ip'] = request.ip
    request['session']['path'] = request.path
    request['session']['counter'] += 1


