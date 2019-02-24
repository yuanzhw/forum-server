import pytest
import secret
from app import configured_app, configured_database
from reset import generate_fake_date, reset_database


@pytest.fixture(scope='session')
def app():
    app = configured_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = configured_database(
        secret.database_username,
        secret.database_password,
        secret.database_host,
        secret.database_test_name,
    )
    with app.app_context():
        reset_database(secret.database_test_name)
        generate_fake_date()
    yield app


@pytest.fixture(scope='session')
def client(app):
    return app.test_client()


class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='yuan', password='123'):
        return self._client.post(
            '/api/user/login',
            json={'username': username, 'password': password}
        )


@pytest.fixture
def auth(client):
    return AuthActions(client)
