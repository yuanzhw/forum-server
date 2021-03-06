from sqlalchemy import Column, String

from models.base_model import SQLMixin, db
from sqlalchemy.orm import relationship


class User(SQLMixin, db.Model):
    """
    User 是一个保存用户数据的 model
    现在只有两个属性 username 和 password
    """

    username = Column(String(50), nullable=False)
    password = Column(String(256), nullable=False)
    email = Column(String(256), nullable=True)
    signature = Column(String(256), nullable=True, default='这家伙很懒，什么都没有留下')
    topics = relationship('Topic')
    reply = relationship('Reply')

    @classmethod
    def salted_password(cls, password, salt='$!@><?>HUI&DWQa`'):
        import hashlib

        def sha256(ascii_str):
            return hashlib.sha256(ascii_str.encode('ascii')).hexdigest()

        hash1 = sha256(password)
        hash2 = sha256(hash1 + salt)
        print('sha256', len(hash2))
        return hash2

    @staticmethod
    def hashed_password(self, pwd):
        import hashlib
        # 用 ascii 编码转换成 bytes 对象
        p = pwd.encode('ascii')
        s = hashlib.sha256(p)
        # 返回摘要字符串
        return s.hexdigest()

    @classmethod
    def register(cls, form):
        name = form.get('username', '')
        pwd = form.get('password', '')
        print(User.one(username=name))
        if len(name) > 2 and User.one(username=name) is None:
            u = User.new(form)
            u.password = u.salted_password(pwd)
            u.save()
            return u
        else:
            return None

    @classmethod
    def validate_login(cls, form):
        user = User.one(username=form['username'])
        if user is not None and user.password == User.salted_password(form['password']):
            return user
        else:
            return None

    def get_detail(self):
        return dict(username=self.username, signature=self.signature, email=self.email)
