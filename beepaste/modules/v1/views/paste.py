import datetime
import json
from sanic import response
from mongoengine.errors import ValidationError, FieldDoesNotExist
from beepaste.modules.v1.models.paste import PasteModel as Paste  # TODO fix
from sanic.views import HTTPMethodView
from beepaste.modules.v1.schemas.paste import pasteSchema
import traceback


class PasteView(HTTPMethodView):

    async def get(self, request, **kwargs):
        ''' fetching paste by pasteid from database '''
        userid = request['userid']
        if userid is None:
            return response.json(
                {'status': 'fail', 'details': 'user is not authenticated'},
                status=401)

        token_limits = request['token_limits']
        source_limits = request['source_limits']

        if source_limits['get_paste'] == 0 or token_limits['get_paste'] == 0:
            return response.json({
                'status': 'fail', 'details': 'Reached maximum limits, wait 15minutes.'},
                status=429)

        try:
            paste_id = kwargs.get('pasteid')
            paste = await Paste.objects(uri=paste_id).first()
            if (paste.toExpire is not True) or ( datetime.datetime.utcnow() <= paste.expiryDate and paste.toExpire is True):
                paste.views += 1
                paste.save()
                paste_obj, errors = pasteSchema().dump(json.loads(paste.to_json()))

                request['token_limits']['get_paste'] -= 1
                request['source_limits']['get_paste'] -= 1

                return response.json(
                    {'status': 'success', 'paste': paste_obj},
                    status=200)
            else:
                # paste.delete()
                return response.json(
                    {'status': 'fail', 'details': "This paste has been expired"},
                    status=410)
                # TOOD: Delete this from database
        except:
            return response.json({'status': 'fail', 'details': "Paste Not found"}, status=404)

    async def post(self, request):
        ''' saves a sent JSON object into database and returns a link to it '''
        print(request.headers)

        userid = request['userid']
        if userid is None:
            return response.json(
                {'status': 'fail', 'details': 'user is not authenticated'},
                status=401)

        token_limits = request['token_limits']
        source_limits = request['source_limits']

        if source_limits['create_paste'] == 0 or token_limits['create_paste'] == 0:
            return response.json({
                'status': 'fail', 'details': 'Reached maximum limits, wait 15minutes.'},
                status=429)
        try:
            input_json = request.json
            safe_data, errors = pasteSchema().load(input_json)

            if errors:
                return response.json(
                    {"status": "fail", "details": errors},
                    status=400)

            new_paste = Paste(**safe_data)
            new_paste.views = 0
            new_paste.ownerID = userid
            await new_paste.generate_url()
            new_paste.validate()
            new_paste.save()
            new_paste_obj, errors = pasteSchema().dump(json.loads(new_paste.to_json()))
            ret_data = {
                'status': 'success',
                'paste': new_paste_obj
            }

            request['token_limits']['create_paste'] -= 1
            request['source_limits']['create_paste'] -= 1

            return response.json(
                {'status': 'success', 'paste': new_paste_obj},
                status=201)
        except ValidationError as e:
            return response.json(
                {'status': 'fail', 'details': 'invalid data',
                    'errors': e.to_dict()},
                status=400)
        # TODO: handle other exceptions!

    async def put(self, request):
        return response.json(
            {'status': 'fail', 'details': 'Method Not Allowed'},
            status=405)

    async def patch(self, request):
        return response.json(
            {'status': 'fail', 'details': 'Method Not Allowed'},
            status=405)

    async def delete(self, request):
        return response.json(
            {'status': 'fail', 'details': 'Method Not Allowed'},
            status=405)
