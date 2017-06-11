from SanicMongo import Document
from SanicMongo.fields import (IntField, DateTimeField, StringField, URLField,
                               BooleanField)


class UserModel(Document):

    email = StringField(required=True, min_length=6, max_length=127)
    password = StringField(required=True, min_length=6, max_length=127)
