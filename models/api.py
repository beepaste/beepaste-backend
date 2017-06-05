import datetime
import string
from random import *

import jwt
from mongomotor import Document, connect
from mongomotor.fields import (EmbeddedDocumentField, FloatField, IntField,
                               ListField, ReferenceField, StringField)


class Api(Document):
    """
    Api model used to authorize api usages!
    """

    secret = StringField(required=True)
    token = StringField(required=True)
    expires = FloatField(required=True) # TODO: expire each Anonymous token after 15 minutes!
    ownerID = IntField(default=0)
    ip_address = StringField(required=True)
    generated_on = FloatField(default=datetime.datetime.utcnow().timestamp())

    __collection__ = "tokens"

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

    def save(self, dbEngine):
        return dbEngine.insert(self.__collection__, json.loads(self.to_json()))

    def countInTime(self, dbEngine, fromTime):
        from_timestamp = fromTime.timestamp()
        query = {
            'ip_address': self.ip_address,
            'expires': {
                '$gt': from_timestamp
            }
        }
        return dbEngine.count(self.__collection__, query)
