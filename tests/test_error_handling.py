async def test_404(test_cli):
    """
    GET request
    """
    resp = await test_cli.post('/some-dummy-route')
    assert resp.status == 404
    resp_json = await resp.json()
    assert resp_json['status'] == 'fail'
