from flask import (
    request,
    redirect,
    url_for,
    Blueprint,
    session,
    abort,
)
from models.user import User
from models.topic import Topic
from utils import response
import status
from routes.helper import current_user, login_required, csrf_required, new_csrf_token

main = Blueprint('topic', __name__)


@main.route('/new', methods=['POST'])
@login_required
@csrf_required
def new():
    form = request.get_json()
    u = current_user()
    Topic.new(form, user_id=u.id)
    data = {'message': 'successful'}
    return response(data=data, status=status.HTTP_201_CREATED)


@main.route('/<int:id>')
@login_required
def detail(id):
    m: Topic = Topic.get(id)
    data = dict(
        id=m.id,
        user_id=m.user_id,
        title=m.title,
        content=m.content,
        views=m.views,
    )
    return response(data=data, status=status.HTTP_200_OK)


@main.route('/delete', methods=['POST'])
@login_required
@csrf_required
def delete():
    id = request.form['id']
    Topic.delete(id=id)
    data = dict(
        message='success'
    )
    return response(data=data, status=status.HTTP_202_ACCEPTED)


@main.route('/list')
def topic_list():
    ms = Topic.all()
    data = list()
    for m in ms:
        m: Topic
        data.append(dict(content=m.content, title=m.title, id=m.id, user_id=m.user_id))
    return response(data=data, status=status.HTTP_200_OK)


@main.route('/csrf')
def csrf_new():
    token = new_csrf_token()
    data = dict(
        token=token
    )
    return response(data=data, status=status.HTTP_200_OK)
