from sanic.views import HTTPMethodView
from sanic import response


class StatView(HTTPMethodView):

    async def get(self, request):
        counter = request['session']['counter']
        path = request['session']['path']
        ip = request['session']['ip']
        return response.json({
                "hello": "world",
                "counter": counter,
                "ip": ip,
                "path": path
                })
