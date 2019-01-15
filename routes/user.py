from flask import (
    request,
    redirect,
    url_for,
    Blueprint,
    session,
    abort,
)
from models.user import User
from utils import response
import status

main = Blueprint('user', __name__)


@main.route("/")
def hello_world():
    session['user_id'] = 'test'
    session.permanent = True
    return "hello world", 400


@main.route('/login', methods=['POST'])
def login():
    form = request.form
    u = User.validate_login(form)
    if u is None:
        # 转到 topic.index 页面
        data = {}
        return response(data, status=status.HTTP_401_UNAUTHORIZED)
    else:
        # session 中写入 user_id
        session['user_id'] = u.id
        # 设置 cookie 有效期为 永久
        session.permanent = True
        data = {'message': 'successful'}
        return response(data, status=status.HTTP_200_OK)


@main.route('register', methods=['POST'])
def register():
    form = request.form
    u = User.register(form)
    data = {'message': 'successful'}
    return response(data=data, status=status.HTTP_201_CREATED)


@main.route('/user/<int:id>')
def user_detail(id):
    u: User = User.one(id=id)
    if u is None:
        abort(404)
    else:
        data = u.get_detail()
        return response(data=data, status=status.HTTP_200_OK)
