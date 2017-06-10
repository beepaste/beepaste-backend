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
    calls = DictField(required=True, default={
        'create_paste': 450,
        'get_paste': 450,
        'delete_pastes': 450,
        'create_user': 3,
        'authenticate_user': 5,
        'get_user_pastes': 90
    })                                  #'''
                                        #    Here we store calls remainig for each token!
                                        #    and they are reseted every 15 minutes.
                                        #    defaults are:
                                        #    {
                                        #        create_paste: 450,
                                        #        get_paste: 450,
                                        #        delete_pastes: 450,
                                        #        create_user: 3,
                                        #        authenticate_user: 5,
                                        #        get_user_pastes: 90,
                                        #    }
                                        #'''

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
