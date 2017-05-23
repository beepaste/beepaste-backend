import yaml
from sanic import Sanic
from sanic.response import json

with open("config.yaml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

web_cnf = cfg['web_server']

# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
app = Sanic()


@app.route("/")
async def test(request):
    return json({"hello": "world"})

if __name__ == "__main__":
    app.run(**web_cnf, log_config=None)