from beepaste import jwt_cnf
import jwt
from beepaste.modules.v1.models.token import TokenModel
from beepaste.redis import redis

async def create_token(userid, exp, ipaddress="127.0.0.1"):
    encoded_token = jwt.encode(
        {'userid': userid, 'exp': exp, 'ip': ipaddress}, jwt_cnf['secret'],
            algorithm=jwt_cnf['algorithm']).decode('utf-8')
    new_token = TokenModel(token=encoded_token)
    await new_token.save()
    await redis.set_value(encoded_token + '_stat', 'valid')
    return encoded_token
