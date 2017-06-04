import datetime
from booby import Model, fields, validators
import string
import jwt
from random import *


class Api(Model):
    """
    Api model used to authorize api usages!
    """

    secret = fields.String(required=True)
    token = fields.String(required=True)
    expires = fields.Float(required=True)
    ownerID = fields.Integer(default=0)
    ip_address = fields.String(required=True)
    generated_on = fields.Float(default=datetime.datetime.utcnow().timestamp())

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
