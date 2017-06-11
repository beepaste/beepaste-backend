import datetime
import json
from sanic import response
from mongoengine.errors import ValidationError
from .models import Paste
from sanic.views import HTTPMethodView
from sanic.response import text


class PasteView(HTTPMethodView):

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

    async def post(self, request):
        ''' saves a sent JSON object into database and returns a link to it '''
        input_json = request.json
        # TODO validation with some lib like marshmallow
        # https://github.com/marshmallow-code/marshmallow
        # not use try catch if validate faild return error from marshmallow
        # else pass to the model
        new_paste = Paste(**input_json)
        try:
            # TODO: set ownerID using the token used to authorize api!
            new_paste.views = 0
            await new_paste.generate_url()
            new_paste.validate()
            new_paste.save()
            new_paste_obj = json.loads(new_paste.to_json())
            ret_data = {
                'status': 'success',
                'paste': new_paste_obj
            }
            return response.json(
                {'status': 'success', 'paste': new_paste_obj},
                status=201)
        except ValidationError as e:
            print(e)
            return response.json(
                    {'status': 'fail', 'details': 'invalid data'},
                    status=400)
        except Exception as e:
            print(e)
            return response.json(
                    {'status': 'fail', 'details': 'server error'},
                    status=500)

    async def put(self, request):
        return text('I am put method')

    async def patch(self, request):
        return text('I am patch method')

    async def delete(self, request):
        return text('I am delete method')
