from sanic.views import HTTPMethodView
from sanic import response
from beepaste.modules.v1.models.user import UserModel
from beepaste.modules.v1.schemas.login import loginSchema
from beepaste.modules.v1.plugins.token import create_token
from beepaste import limits_cnf
import datetime

class AuthView(HTTPMethodView):

    async def get(self, request):
        ''' User Profile'''
        userid = request['userid']
        if userid is None:
            return response.json(
                {"status": "fail", "details": "not authorized"},
                status=401)
        elif userid == 0:
            return response.json(
                    {'status': 'success', 'userid': userid, 'description': 'this is anonymous user!'})
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
        input_json = request.json
        if type(input_json == None):
            input_json = {}
        if input_json != {}:
            #Login attempt
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
                    encoded_token = await create_token(userid, datetime.datetime.utcnow() +
                                                datetime.timedelta(minutes=limits_cnf['auth_timeout'] / 60),
                                                request.ip[0])
                    return response.json(
                        {'status': 'success', "X-TOKEN": encoded_token},
                        status=200)
        else:
            #Guest
            encoded_token = await create_token(0, datetime.datetime.utcnow() +
                                                datetime.timedelta(minutes=limits_cnf['reset_timeout'] / 60),
                                                request.ip[0])
            return response.json(
                {'status': 'success', "X-TOKEN": encoded_token},
                status=200)
