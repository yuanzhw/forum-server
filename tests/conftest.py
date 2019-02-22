import pytest
import secret
from app import configured_app
from sqlalchemy import create_engine
from models.base_model import db
from reset import generate_fake_date


@pytest.fixture(scope='session')
def app():
    app = configured_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:{}@localhost/forum_test?charset=utf8mb4'.format(
        secret.database_password
    )
    with app.app_context():
        reset_database()
        generate_fake_date()
    yield app


@pytest.fixture(scope='session')
def client(app):
    return app.test_client()


def reset_database():
    url = 'mysql+pymysql://root:{}@localhost/?charset=utf8mb4'.format(secret.database_password)
    e = create_engine(url, echo=True)

    with e.connect() as c:
        c.execute('DROP DATABASE IF EXISTS forum_test')
        c.execute('CREATE DATABASE forum_test CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci')
        c.execute('USE forum_test')

    db.metadata.create_all(bind=e)


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
