from flask import Flask
from routes.user import main as user_routes
from routes.topic import main as topic_routes
from routes.helper import main as helper_routes
from models.base_model import db
import secret


def configured_app():
    flask_app = Flask(__name__)
    flask_app.config['TEMPLATES_AUTO_RELOAD'] = True
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    flask_app.jinja_env.auto_reload = True
    flask_app.secret_key = secret.secret_key

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:{}@localhost/forum?charset=utf8mb4'.format(
        secret.database_password
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
    app.register_blueprint(helper_routes,url_prefix='/api')


if __name__ == '__main__':
    app = configured_app()
    config = dict(
        debug=True,
        host='localhost',
        port=2000,
    )
    app.run(**config)
