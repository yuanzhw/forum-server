import time

from sqlalchemy import Column, Integer, UnicodeText, ForeignKey

from models.base_model import db, SQLMixin
from models.user import User


class Reply(SQLMixin, db.Model):
    content = Column(UnicodeText, nullable=False)
    topic_id = Column(Integer, ForeignKey('topic.id', ondelete='CASCADE'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)

    def user(self):
        u: User = User.one(id=self.user_id)
        return u

    @classmethod
    def new(cls, form, user_id):
        form['user_id'] = user_id
        m = super().new(form)
        return m
