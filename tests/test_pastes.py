import json, asyncio

async def test_post_unauthenticated(test_cli):
    resp = await test_cli.get('/api/v1/paste')
    assert resp.status == 401

async def test_get_unauthenticated(test_cli):
    resp = await test_cli.get('/api/v1/paste/auis35')
    assert resp.status == 401

async def test_create_paste_successfully(test_cli):
    resp = await test_cli.post('/api/v1/auth')
    resp_json = await resp.json()
    new_paste = {
        'title': "some-rnd-title",
        'expireAfter': 60,
        'toExpire': True,
        'raw': 'hello world!'
    }
    resp = await test_cli.post('/api/v1/paste', headers={'X-TOKEN': resp_json['X-TOKEN']}, data=json.dumps(new_paste))
    assert resp.status == 201
    resp_json = await resp.json()
    assert resp_json['status'] == 'success'

async def test_create_and_get_paste_successfully(test_cli):
    resp = await test_cli.post('/api/v1/auth')
    resp_json = await resp.json()
    token = resp_json['X-TOKEN']
    new_paste = {
        'title': "some-rnd-title",
        'expireAfter': 60,
        'toExpire': True,
        'raw': 'hello world!'
    }
    resp = await test_cli.post('/api/v1/paste', headers={'X-TOKEN': token}, data=json.dumps(new_paste))
    resp_json = await resp.json()
    url = "/api/v1/paste/{}".format(resp_json['paste']['uri'])
    resp = await test_cli.get(url, headers={'X-TOKEN': token})
    assert resp.status == 200
    assert resp_json['status'] == 'success'

async def test_create_paste_without_raw(test_cli):
    resp = await test_cli.post('/api/v1/auth')
    resp_json = await resp.json()
    new_paste = {
        'title': "some-rnd-title",
        'expireAfter': 60,
        'toExpire': True
    }
    resp = await test_cli.post('/api/v1/paste', headers={'X-TOKEN': resp_json['X-TOKEN']}, data=json.dumps(new_paste))
    assert resp.status == 400
    resp_json = await resp.json()
    assert resp_json['status'] == 'fail'

async def test_create_and_get_paste_with_timeout_successfully(test_cli):
    resp = await test_cli.post('/api/v1/auth')
    resp_json = await resp.json()
    token = resp_json['X-TOKEN']
    new_paste = {
        'title': "some-rnd-title",
        'expireAfter': 2,
        'toExpire': True,
        'raw': 'hello world!'
    }
    resp = await test_cli.post('/api/v1/paste', headers={'X-TOKEN': token}, data=json.dumps(new_paste))
    resp_json = await resp.json()
    print(resp_json)
    url = "/api/v1/paste/{}".format(resp_json['paste']['uri'])
    await asyncio.sleep(3)
    resp = await test_cli.get(url, headers={'X-TOKEN': token})
    resp_json = await resp.json()
    assert resp.status == 410
    assert resp_json['status'] == 'fail'