import asyncio_redis
from beepaste.utils.logger import lg
from beepaste import redis_cnf


class Redis:
    """
    A simple wrapper class that allows you to share a connection
    pool across your application.
    """
    _pool = None

    async def get_redis_pool(self):
        if not self._pool:
            self._pool = await asyncio_redis.Pool.create(**redis_cnf)
            await lg(1, 'connected to redis')

        return self._pool


redis = Redis()
