# project/models.py


import datetime

from project import db, bcrypt


class Song(db.Model):

    __tablename__ = "song"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(255), nullable=False)
    requester = db.Column(db.String(255), nullable=False)
    delay = db.Column(db.INTEGER(), nullable=False)
    #     mode_id = db.Column(db.Integer, db.ForeignKey('mode.id'))

    def __init__(self, url, requester, delay):
        self.url = url
        self.requester = requester
        self.delay = delay

    def __repr__(self):
        return '<url {0}>'.format(self.url)


# class User(db.Model):
#
#     __tablename__ = "users"
#
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     email = db.Column(db.String(255), unique=True, nullable=False)
#     password = db.Column(db.String(255), nullable=False)
#     registered_on = db.Column(db.DateTime, nullable=False)
#     admin = db.Column(db.Boolean, nullable=False, default=False)
#
#     def __init__(self, email, password, admin=False):
#         self.email = email
#         self.password = bcrypt.generate_password_hash(password)
#         self.registered_on = datetime.datetime.now()
#         self.admin = admin
#
#     def is_authenticated(self):
#         return True
#
#     def is_active(self):
#         return True
#
#     def is_anonymous(self):
#         return False
#
#     def get_id(self):
#         return self.id
#
#     def __repr__(self):
#         return '<User {0}>'.format(self.email)
