import yaml
from sanic import Sanic
from sanic.response import json

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

api_config = cfg['api']


# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
app = Sanic()


@app.route("/")
async def test(request):
    print(request.headers)
    return json({"hello": "world"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
