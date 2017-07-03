import asyncio_redis
from beepaste.utils.logger import lg
from beepaste import redis_cnf
import json


class Redis:
    """
    A simple wrapper class that allows you to share a connection
    pool across your application.
    """
    _pool = None

    async def set_value(self, key, data):
        conn = await self.get_redis_pool()
        await conn.set(key, data)

    async def get_value(self, key):
        conn = await self.get_redis_pool()
        data = await conn.get(key)

    async def get_dict(self, key):
        # get str and convert to json
        value = await self.get_value(key)

        data = json.loads(value)
        return data

    async def set_dict(self, key, data):
        # set value of key, a dict object!
        value = json.dumps(data)

        await self.set_value(key, value)

    async def get_redis_pool(self):
        if not self._pool:
            self._pool = await asyncio_redis.Pool.create(**redis_cnf)
            # await lg(1, 'connected to redis')

        return self._pool


redis = Redis()
