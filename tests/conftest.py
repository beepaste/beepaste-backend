import pytest
from beepaste import app
from sanic.websocket import WebSocketProtocol

@pytest.yield_fixture
def app_server():
    yield app

@pytest.fixture
def test_cli(loop, app_server, test_client):
    return loop.run_until_complete(test_client(app, protocol=WebSocketProtocol))
