from sanic.views import HTTPMethodView
from sanic import response


class DocView(HTTPMethodView):

    async def get(self, request):
        return response.json({
                "desc": "some api document swager open api",
                })
