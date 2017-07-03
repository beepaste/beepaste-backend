from sanic.views import HTTPMethodView
from sanic import response


class StatView(HTTPMethodView):

    async def get(self, request):
        counter = request['stat']['counter']
        path = request['stat']['path']
        ip = request['stat']['ip']
        return response.json({
                "hello": "world",
                "counter": counter,
                "ip": ip,
                "path": path
                })
