from SanicMongo import Document
from SanicMongo.fields import (IntField, DateTimeField, StringField, URLField,
                               BooleanField)


class UserModel(Document):

    email = StringField(required=True, min_length=6, max_length=127)
    password = StringField(required=True, min_length=6, max_length=127)

    async def authorize(email, password):
        # TODO check user by email and pass if success return userid else none
        if email == 'admin@beepaste.com' and password == "admin":
            userid = 1
            return userid
        else:
            return None

    async def getById(userid):
        # TODO get user id from mongodb and return safe parameter
        return {
                "name": "beepaste",
                "somthing": "somedata from user"
                }
