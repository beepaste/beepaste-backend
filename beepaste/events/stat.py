from beepaste.plugins.stat.stat import RedisStatInterface
from beepaste import app
from beepaste.redis import redis

# pass the getter method for the connection pool into the session
session_interface = RedisStatInterface(redis.get_redis_pool)


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
