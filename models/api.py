import datetime
import string
from random import *

import jwt
from asymongo import Document, connect
from asymongo.fields import (IntField, DateTimeField, StringField)


class Api(Document):
    """
    Api model used to authorize api usages!
    """

    secret = StringField(required=True)
    token = StringField(required=True)
    expires = DateTimeField(required=True, default=(datetime.datetime.utcnow() + datetime.timedelta(minutes=15))) # TODO: expire each Anonymous token after 15 minutes!
    ownerID = IntField(default=0)
    ip_address = StringField(required=True)
    generated_on = DateTimeField(default=datetime.datetime.utcnow())

    meta = {'collection': 'tokens'}

    def genSecret(self, len=8):
        allchar = string.ascii_letters + string.digits
        self.secret = "".join(choice(allchar) for x in range(len))

    def genToken(self):
        payload = {
            'exp': self.expires,
            'iat': datetime.datetime.utcnow(),
            'ownerID': self.ownerID
        }
        self.token = jwt.encode(payload, self.secret, algorithm='HS256').decode('utf-8')
