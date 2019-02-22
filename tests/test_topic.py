from flask import request


def test_topic_create(client, auth, app):
    data = dict(content='content_test', title='title_test')
    rv = client.post('/api/topic/new', json=data)
    assert b'login required' in rv.data
    auth.login()
    csrf_token = client.cookie_jar._cookies.get('localhost.local').get('/').get('csrf_token').value
    rv = client.post('/api/topic/new', json=data)
    assert b'401 Unauthorized' in rv.data
    rv = client.post('/api/topic/new' + '?token=' + csrf_token, json=data)
    assert b'successful' in rv.data
    rv = client.get('/api/topic/list')
    assert b'"content": "content_test"' in rv.data
