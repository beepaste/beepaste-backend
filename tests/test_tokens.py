async def test_get_token_post_request(test_cli):
    """
    POST request
    """
    resp = await test_cli.post('/api/v1/auth')
    assert resp.status == 200
    resp_json = await resp.json()
    assert resp_json['status'] == 'success'

async def test_get_token_get_request(test_cli):
    """
    GET request
    """
    resp = await test_cli.post('/api/v1/auth')
    assert resp.status == 200
    resp_json = await resp.json()
    assert resp_json['status'] == 'success'
    resp = await test_cli.get('/api/v1/auth', headers={'X-TOKEN': resp_json['X-TOKEN']})
    assert resp.status == 200
    resp_json = await resp.json()
    assert resp_json['status'] == 'success'
