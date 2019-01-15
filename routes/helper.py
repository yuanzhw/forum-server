import functools
import uuid
from functools import wraps

from flask import session, request, abort, redirect, url_for

from models.user import User
from utils import log
import redis

csrf_tokens = redis.StrictRedis()


def login_required(route_function):
    """
    这个函数看起来非常绕，所以你不懂也没关系
    就直接拿来复制粘贴就好了
    """

    @functools.wraps(route_function)
    def f():
        log('login_required')
        u = current_user()
        if u is None:
            log('游客用户')
            return redirect(url_for('index.index'))
        else:
            log('登录用户', route_function)
            return route_function()

    return f


def current_user():
    uid = session.get('user_id', '')
    u: User = User.one(id=uid)
    # type annotation
    # User u = User.one(id=uid)
    return u


# csrf_tokens = dict()


def csrf_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.args['token']

        u = current_user()
        if csrf_tokens.exists(token) and csrf_tokens.get(token) == u.id:
            csrf_tokens.delete(token)
            return f(*args, **kwargs)
        else:
            abort(401)

    return wrapper


def new_csrf_token():
    u = current_user()
    token = str(uuid.uuid4())
    csrf_tokens.set(token, u.id)
    return token
