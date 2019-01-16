from sqlalchemy import Column, String, ForeignKey, Integer, UnicodeText, Unicode

from models.base_model import SQLMixin, db
from sqlalchemy.orm import relationship


class Topic(SQLMixin, db.Model):
    title = Column(Unicode(50), nullable=False)
    content = Column(UnicodeText(5000), nullable=False)
    views = Column(Integer,nullable=False, default=0)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    reply = relationship('Reply')


class Reply(SQLMixin, db.Model):
    content = Column(String(500), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    topic_id = Column(Integer, ForeignKey('topic.id', ondelete='CASCADE'), nullable=False)
