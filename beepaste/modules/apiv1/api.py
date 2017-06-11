import datetime
import string
from random import *

import jwt
from SanicMongo import Document
from SanicMongo.fields import (IntField, DateTimeField, StringField, DictField)


class Api(Document):
    """
    Api model used to authorize api usages!
    """

    secret = StringField(required=True)
    token = StringField(required=True)
    expires = DateTimeField(required=True, default=
                            (datetime.datetime.utcnow() + datetime.timedelta(minutes=15)))
                            # TODO: expire each Anonymous token after 15 minutes!
                            # TODO: no more than 2 tokens each 15 minutes for each ip
    ownerID = IntField(default=0)
    ip_address = StringField(required=True)
    generated_on = DateTimeField(default=datetime.datetime.utcnow())

    meta = {'collection': 'tokens'}

    def genSecret(self, len=16):
        allchar = string.ascii_letters + string.digits
        self.secret = "".join(choice(allchar) for x in range(len))

    def genToken(self):
        payload = {
            'exp': self.expires,
            'iat': datetime.datetime.utcnow(),
            'ownerID': self.ownerID
        }
        self.token = jwt.encode(payload, self.secret, algorithm='HS256').decode('utf-8')
