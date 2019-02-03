from sqlalchemy import Column, String, ForeignKey, Integer, UnicodeText, Unicode

from models.base_model import SQLMixin, db
from models.user import User
from sqlalchemy.orm import relationship


class Topic(SQLMixin, db.Model):
    title = Column(Unicode(50), nullable=False)
    content = Column(UnicodeText(5000), nullable=False)
    views = Column(Integer, nullable=False, default=0)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    reply = relationship('Reply')

    @classmethod
    def new(cls, form, user_id):
        form['user_id'] = user_id
        m = super().new(form)
        return m

    @classmethod
    def get(cls, id):
        m: Topic = cls.one(id=id)
        m.views += 1
        m.save()
        return m

    def user(self):
        u = User.one(id=self.user_id)
        return u

    def replies(self):
        ms = Reply.all(topic_id=self.id)
        return ms

    def reply_count(self):
        count = len(self.replies())
        return count
