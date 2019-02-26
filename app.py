from flask import Flask
from routes.user import main as user_routes
from routes.topic import main as topic_routes
from routes.helper import main as helper_routes
from routes.reply import main as reply_routes
from routes.message import main as message_routes
from models.base_model import db
from flask_cors import CORS
import secret


def configured_database(database_username, database_password, host, database_name, database_charset='utf8mb4'):
    return 'mysql+pymysql://{}:{}@{}/{}?charset={}'.format(database_username,
                                                           database_password,
                                                           host,
                                                           database_name,
                                                           database_charset)


def configured_app():
    flask_app = Flask(__name__)
    CORS(flask_app, supports_credentials=True)
    flask_app.config['TEMPLATES_AUTO_RELOAD'] = True
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    flask_app.jinja_env.auto_reload = True
    flask_app.secret_key = secret.secret_key

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = configured_database(
        secret.database_username,
        secret.database_password,
        secret.database_host,
        secret.database_name,
    )

    db.init_app(flask_app)
    flask_app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    register_routes(flask_app)
    return flask_app


def register_routes(app):
    """
    在 flask 中，模块化路由的功能由 蓝图（Blueprints）提供
    蓝图可以拥有自己的静态资源路径、模板路径（现在还没涉及）
    用法如下
    """
    # 注册蓝图
    # 有一个 url_prefix 可以用来给蓝图中的每个路由加一个前缀

    app.register_blueprint(user_routes, url_prefix='/api/user')
    app.register_blueprint(topic_routes, url_prefix='/api/topic')
    app.register_blueprint(reply_routes, url_prefix='/api/reply')
    app.register_blueprint(message_routes, url_prefix='/api/message')
    app.register_blueprint(helper_routes, url_prefix='/api')


if __name__ == '__main__':
    app = configured_app()
    config = dict(
        debug=True,
        host='localhost',
        port=2000,
    )
    app.run(**config)
