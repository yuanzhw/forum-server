from sqlalchemy import Column, String, ForeignKey, Integer

from models.base_model import SQLMixin, db
from sqlalchemy.orm import relationship


class Topic(SQLMixin, db.Model):
    title = Column(String(50), nullable=False)
    context = Column(String(5000), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    reply = relationship('Reply')


class Reply(SQLMixin, db.Model):
    content = Column(String(500), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    topic_id = Column(Integer, ForeignKey('topic.id', ondelete='CASCADE'), nullable=False)
