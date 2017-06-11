import ujson
from beepaste.plugins.stat import BaseSessionInterface, SessionDict
from typing import Callable


class RedisStatInterface(BaseSessionInterface):
    def __init__(
            self,
            redis_getter: Callable,
            expiry: int = 2592000,
            prefix: str='stat:'):
        self.redis_getter = redis_getter
        self.expiry = expiry
        self.prefix = prefix

    async def open(self, request):
        sid = request.ip[0]

        stat_dict = SessionDict(sid=sid)
        redis_connection = await self.redis_getter()
        val = await redis_connection.get(self.prefix + sid)

        if val is not None:
            data = ujson.loads(val)
            stat_dict = SessionDict(data, sid=sid)
        else:
            stat_dict = SessionDict(sid=sid)

        request['stat'] = stat_dict
        return stat_dict

    async def save(self, request, response) -> None:
        if 'stat' not in request:
            return

        redis_connection = await self.redis_getter()
        key = self.prefix + request['stat'].sid

        val = ujson.dumps(dict(request['stat']))

        await redis_connection.setex(key, self.expiry, val)
