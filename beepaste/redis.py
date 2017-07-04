import aioredis
from beepaste.utils.logger import lg
from beepaste import redis_cnf
import json


class Redis:
    """
    A simple wrapper class that allows you to share a connection
    pool across your application.
    """
    _connection = None

    async def get_connection(self):
        if not self._connection:
            self._connection = await aioredis.create_redis(**redis_cnf)
            # await lg(1, 'connected to redis')

        return self._connection

    async def expire(self, key, ttl):
        conn = await self.get_connection()
        await conn.expire(key, ttl)

    async def set_value(self, key, data):
        conn = await self.get_connection()
        await conn.set(key, data)

    async def set_dict(self, key, data):
        # set value of key, a dict object!
        value = json.dumps(data)

        await self.set_value(key, value)

    async def get_value(self, key):
        conn = await self.get_connection()
        data = await conn.get(key)

        return data

    async def get_dict(self, key):
        # get str and convert to json
        value = await self.get_value(key)

        data = json.loads(value)
        return data

    async def exists(self, key):
        # check if key exists!
        conn = await self.get_connection()
        stat = await conn.exists(key)

        return stat


redis = Redis()
