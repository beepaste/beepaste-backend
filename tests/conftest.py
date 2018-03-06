import pytest
import asyncio
from beepaste import app
from sanic.websocket import WebSocketProtocol

@pytest.yield_fixture
def app_srv():
    yield app

@pytest.fixture
def test_cli(loop, app_srv, test_client):
    return loop.run_until_complete(test_client(app_srv, protocol=WebSocketProtocol))

@pytest.fixture
def sanic_server(loop, app_srv, test_server):
    return loop.run_until_complete(test_server(app_srv))

@pytest.fixture
def loop():
    loop = asyncio.get_event_loop()
    yield loop