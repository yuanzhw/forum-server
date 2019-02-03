from flask import (
    request,
    redirect,
    url_for,
    Blueprint,
)
from utils import response
import status
from models.reply import Reply
from routes.helper import current_user, login_required, csrf_required, new_csrf_token

main = Blueprint('reply', __name__)


@main.route('/new', methods=['POST'])
@login_required
@csrf_required
def add():
    u = current_user()
    form = request.get_json()
    Reply.new(form, u.id)
    data = 'reply create successfully'
    return response(data=data, status=status.HTTP_201_CREATED)


@main.route('/list/<int:topic_id>')
@login_required
def reply_list(topic_id):
    ms = Reply.all(topic_id=topic_id)
    data = list()
    for m in ms:
        m: Reply
        data.append(dict(content=m.content, user_id=m.user_id, topic_id=m.topic_id, username=m.user().username))
    return response(data=data, status=status.HTTP_200_OK)
