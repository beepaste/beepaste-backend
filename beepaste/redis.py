import asyncio_redis
from beepaste import logger
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
            logger.info('connedted to redis')

        return self._pool


redis = Redis()
