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
from routes.helper import login_required, new_csrf_token
import status

main = Blueprint('user', __name__)


@main.route("/")
def hello_world():
    session['user_id'] = 'test'
    session.permanent = True
    return "hello world", 400


@main.route('/login', methods=['POST'])
def login():
    form = request.get_json()
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
        res = response(data, status=status.HTTP_200_OK)
        csrf_token = new_csrf_token()
        res.set_cookie("csrf_token", csrf_token)
        return res


@main.route('register', methods=['POST'])
def register():
    form = request.form
    u = User.register(form)
    data = {'message': 'successful'}
    return response(data=data, status=status.HTTP_201_CREATED)


@main.route('/user/<int:id>')
@login_required
def user_detail(id):
    u: User = User.one(id=id)
    if u is None:
        abort(404)
    else:
        data = u.get_detail()
        return response(data=data, status=status.HTTP_200_OK)
