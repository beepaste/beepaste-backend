from sanic.views import HTTPMethodView
from sanic import response
from .models import UserModel
import jwt


class AuthView(HTTPMethodView):

    async def get(self, request):

        # TODO get from db
        userid = 1
        # TODO add secret algorithm from config
        encoded = jwt.encode({'userid': userid}, 'secret', algorithm='HS256')
        return response.json({
                "jwt": encoded,
                })
