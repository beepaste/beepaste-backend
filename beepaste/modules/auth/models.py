from SanicMongo import Document
from SanicMongo.fields import (EmailField, DateTimeField, StringField, IntField)
import datetime
import json
from passlib.hash import sha512_crypt
# TODO: add more fields to model!
# TODO: enable oauth


class UserModel(Document):

    userid = IntField(required=True, primary_key=True)
    email = EmailField(required=True, min_length=6, max_length=127, unique=True)
    password = StringField(required=True, min_length=6, max_length=127)
    username = StringField(required=True, min_length=6, max_length=30,
                           unique=True)
    registered = DateTimeField(default=datetime.datetime.utcnow())

    async def authorize(username, password):
        curr_user = await UserModel.objects(username=username).first()
        if curr_user is not None:
            if sha512_crypt.verify(password, curr_user.password):
                userid = curr_user.userid
            else:
                userid = None
            return userid
        else:
            return None

    async def getById(userid):
        curr_user = await UserModel.objects(username=username).first()
        if curr_user is not None:
            ret_data_json = curr_user.to_json()
            ret_data = json.loads(ret_data_json)
            return ret_data
        else:
            return None

    async def setPassword(self, password):
        self.password = sha512_crypt.hash(password)
