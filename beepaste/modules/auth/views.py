from sanic.views import HTTPMethodView
from sanic import response
from .models import UserModel
import jwt
from .schemas import loginSchema


class AuthView(HTTPMethodView):

    async def get(self, request):
        userid = request['userid']
        if userid is None:
            return response.json({
                "success" : "false",
                "error" : "x",
                "msg" : "you are not login",
                "desc" : "send token with X-TOKEN header parameter"
                })
        else:
            return response.json({
                "user": "profile"
                })

    async def post(self, request):

        input_json = request.json
        safe_data, errors = loginSchema().load(input_json)
        if errors :
            return response.json({
                "success" : "false",
                "msg" : errors
                })
        else:
            userid = await UserModel.authorize(
                    safe_data['email'], safe_data['password'])

            if userid is None:
                return response.json({
                    "success": "false",
                    "msg": "wrong password"
                    })
            else:
                # TODO add secret algorithm from config
                encoded = jwt.encode(
                        {'userid': userid}, 'secret', algorithm='HS256')
                return response.json({
                        "X-TOKEN": encoded,
                        })
