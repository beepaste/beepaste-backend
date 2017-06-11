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
    expires = DateTimeField(required=True, default=(datetime.datetime.utcnow() +
                            datetime.timedelta(minutes=15)))
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
        self.token = jwt.encode(payload, self.secret,
                                algorithm='HS256').decode('utf-8')



async def new_api_token(request):
    try:
        limits = get_config('limits')
    except Exception:
        logger.critical('config file not found.. aborting')
        return resp.json(
            {'status': 'fail', 'details': 'server error'},
            status=500)
    try:
        all_keys = await redis.redis.connection.mget_aslist(request.ip)
        if len(all_keys) < limits.get(token_for_ip):
            new_api = Api()
            new_api.genSecret()
            new_api.genToken()
            await redis.redis.connection.set(request.ip, new_api.token)
            redis.redis.connection.expire(request.ip, limits.get(reset_timeout))
            new_api.save()
        else:
            logger.info('too many connections for ip{}'.format(request.ip))
            return resp.json(
                {'status': 'fail', 'details': 'too many connections'},
                status=201)
    except Exception:
        logger.critical('connection to Redis failed')
        return resp.json(
            {'status': 'fail', 'details': 'server error'},
            status=500)
    # TODO move to another modules
    '''
    generates new api-key if it was ok
    (no more than 5 tokens in 15minutes)
    '''
    return resp.json({'stat': 'received'})
