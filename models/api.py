import datetime
from booby import Model, fields, validators
import string
import jwt

class Date(fields.Field):
    def __init__(self, *args, **kwargs):
        super(Date, self).__init__(validators.DateTime(), *args, **kwargs)

class Api(Model):
    """
    Api model used to authorize api usages!
    """

    secret = fields.String(required=True)
    token = fields.String(required=True)
    expires = Date(required=True)
    ownerID = fields.Integer(default=0)
    ip_address = fields.String(required=True)

    def genSecret(self, len):
        allchar = string.ascii_lowercase + string.digits
        self.secret = "".join(choice(allchar) for x in range(len))

    def genToken(self):
        payload = {
            'exp': self.expires,
            'iat': datetime.datetime.utcnow(),
            'ownerID': self.ownerID
        }
        self.token = jwt.encode(payload, self.secret, algorithm='HS256')
