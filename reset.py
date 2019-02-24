from sqlalchemy import create_engine

import secret
from app import configured_app, configured_database
from models.base_model import db
from models.user import User


def reset_database(database_name=secret.database_name):
    url = configured_database(
        secret.database_username,
        secret.database_password,
        secret.database_host,
        database_name,
    )
    print(url)
    e = create_engine(url, echo=True)

    with e.connect() as c:
        c.execute('DROP DATABASE IF EXISTS {}'.format(database_name))
        c.execute('CREATE DATABASE {} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci'.format(database_name))
        c.execute('USE {}'.format(database_name))

    db.metadata.create_all(bind=e)


def generate_fake_date():
    form = dict(
        username='yuan',
        password='123'
    )
    u = User.register(form)
    print(u)


if __name__ == '__main__':
    app = configured_app()
    with app.app_context():
        reset_database()
        generate_fake_date()
