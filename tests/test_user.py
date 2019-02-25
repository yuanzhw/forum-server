def test_login(client):
    data = dict(username='yuan', password='123')
    rv = client.post('/api/user/login', json=data)
    assert b'successful' in rv.data
    data = dict(username='yuan', password='234')
    rv = client.post('/api/user/login', json=data)
    assert b'invalid username or password' in rv.data


def test_register(client):
    data = dict(username='yuanzw', password='123')
    rv = client.post('/api/user/register', json=data)
    assert b'successful' in rv.data
    rv = client.post('/api/user/login', json=data)
    assert b'successful' in rv.data
    rv = client.post('/api/user/register', json=data)
    assert b'register failed' in rv.data


def test_detail(client, auth):
    auth.login()
    rv = client.get('/api/user/detail')
    assert b'yuan' in rv.data


def test_update(client, auth):
    auth.login()
    data = dict(email='yuanzhw@vip.qq.com')
    rv = client.post('/api/user/update', json=data)
    assert b'update success' in rv.data
    rv = client.get('/api/user/detail')
    assert b'yuanzhw@vip.qq.com' in rv.data


def test_user_detail(client):
    rv = client.get('api/user/1')
    assert b'yuan' in rv.data
