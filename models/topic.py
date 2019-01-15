from sqlalchemy import Column, String, ForeignKey, Integer

from models.base_model import SQLMixin, db


class Topic(SQLMixin, db.Model):
    title = Column(String(50), nullable=False)
    context = Column(String(5000), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))