from beepaste import app
from random import randint


@app.middleware('request')
async def add_analytic_to_session(request):
    # TODO remove this shit :)
    if not request['stat'].get('counter'):
        request['stat']['counter'] = 0
    request['stat']['ip'] = request.ip
    request['stat']['path'] = request.path
    request['stat']['counter'] += 1
