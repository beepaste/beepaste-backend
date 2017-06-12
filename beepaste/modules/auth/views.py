from sanic.views import HTTPMethodView
from sanic import response
from .models import UserModel
import jwt
from .schemas import loginSchema
from beepaste import jwt_cnf


class AuthView(HTTPMethodView):

    async def get(self, request):
        ''' User Profile'''

        userid = request['userid']
        if userid is None or userid == 0:
            return response.json(
                {"status": "fail", "details": "not authorized"},
                status=401)
        else:
            user = UserModel.getById(userid)
            if user is not None:
                user.pop('password', None)
                return response.json(
                            {'status': 'success', 'user': user})
            else:
                return response.json(
                    {'status': 'fail', 'details': 'no such user found'},
                    status=400)

    async def post(self, request):
        '''this is for login , logout not required for token base auth'''
        # TODO: generate token for anonymous users based on ip!
        input_json = request.json
        safe_data, errors = loginSchema().load(input_json)
        if errors:
            return response.json(
                {"status": "fail", "details": errors},
                status=400)
        else:
            userid = await UserModel.authorize(
                    safe_data['username'], safe_data['password'])

            if userid is None:
                return response.json(
                    {"status": "fail", "details": "wrong username or password"},
                    status=403)
            else:
                encoded = jwt.encode(
                        {'userid': userid}, jwt_cnf['secret'],
                        algorithm=jwt_cnf['algorithm'])
                # TODO: save generated token to database (both redis and mongo)
                # TODO: generate secret-key for each token!
                return response.json(
                        {'status': 'success', "X-TOKEN": encoded})
