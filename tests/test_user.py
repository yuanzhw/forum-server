def test_login(client):
    data = dict(username='yuan', password='123')
    rv = client.post('/api/user/login', json=data)
    assert b'successful' in rv.data


def test_register(client):
    data = dict(username='yuanzw', password='123')
    rv = client.post('/api/user/register', json=data)
    assert b'successful' in rv.data
    rv = client.post('/api/user/login', json=data)
    assert b'successful' in rv.data
