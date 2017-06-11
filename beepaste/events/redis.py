from sanic_session import RedisSessionInterface
import asyncio_redis
from beepaste import app


class Redis:
    """
    A simple wrapper class that allows you to share a connection
    pool across your application.
    """
    _pool = None

    async def get_redis_pool(self):
        if not self._pool:
            # TODO load setting from config
            self._pool = await asyncio_redis.Pool.create(
                host='localhost', port=6379, poolsize=10, db=0
            )

        return self._pool


redis = Redis()

# pass the getter method for the connection pool into the session
session_interface = RedisSessionInterface(redis.get_redis_pool)


@app.middleware('request')
async def add_session_to_request(request):
    # before each request initialize a session
    # using the client's request
    await session_interface.open(request)


@app.middleware('response')
async def save_session(request, response):
    # after each request save the session,
    # pass the response to set client cookies
    await session_interface.save(request, response)
