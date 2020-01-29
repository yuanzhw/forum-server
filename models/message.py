import time

from sqlalchemy import Column, Integer, UnicodeText, ForeignKey, Boolean

from models.base_model import db, SQLMixin
from models.user import User


class Message(SQLMixin, db.Model):
    content = Column(UnicodeText, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    read = Column(Boolean, default=False, nullable=False)

    def user(self):
        u: User = User.one(id=self.user_id)
        return u

    @classmethod
    def get(cls, message_id):
        m: Message = cls.one(id=message_id)
        m.read = True
        m.save()
        return m

    @classmethod
    def get_unread_num(cls, user_id):
        ms = cls.all(user_id=user_id, read=False)
        return len(ms)

    @classmethod
    def read_all(cls, user_id):
        ms = Message.all(user_id=user_id)
        for m in ms:
            m: Message
            m.read = True
            m.save()
