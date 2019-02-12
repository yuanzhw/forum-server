from flask import (
    request,
    redirect,
    url_for,
    Blueprint,
)
from utils import response
import status
from models.message import Message
from routes.helper import current_user, login_required, csrf_required, new_csrf_token

main = Blueprint('message', __name__)


@main.route('/list')
@login_required
def reply_list():
    u = current_user()
    ms = Message.all(user_id=u.id)
    data = list()
    for m in ms:
        m: Message
        data.append(dict(id=m.id,
                         content=m.content,
                         user_id=m.user_id,
                         read=m.read,
                         create_time=m.created_time, ))
    return response(data=data, status=status.HTTP_200_OK)


@main.route('/unread')
@login_required
def unread_num():
    u = current_user()
    num = Message.get_unread_num(u.id)
    data = dict(unread=num)
    return response(data=data, status=status.HTTP_200_OK)


@main.route('/<int:id>')
@login_required
def read(id):
    m = Message.get(message_id=id)
    data = dict(id=m.id,
                content=m.content,
                user_id=m.user_id,
                read=m.read,
                create_time=m.created_time, )
    return response(data=data, status=status.HTTP_200_OK)
