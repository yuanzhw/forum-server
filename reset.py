from sqlalchemy import create_engine

import secret
from app import configured_app
from models.base_model import db
from models.user import User
from models.topic import Topic


def reset_database():
    url = 'mysql+pymysql://root:{}@localhost/?charset=utf8mb4'.format(secret.database_password)
    e = create_engine(url, echo=True)

    with e.connect() as c:
        c.execute('DROP DATABASE IF EXISTS forum')
        c.execute('CREATE DATABASE forum CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci')
        c.execute('USE forum')

    db.metadata.create_all(bind=e)


def generate_fake_date():
    form = dict(
        username='gua',
        password='123'
    )
    u = User.register(form)
    print(u)


if __name__ == '__main__':
    app = configured_app()
    with app.app_context():
        reset_database()
        generate_fake_date()
