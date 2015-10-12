from project import db


class SongRequest(db.Model):

    __tablename__ = "song_request"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    delay = db.Column(db.INTEGER(), nullable=False)
    requester = db.Column(db.String(255), nullable=False)
    song_file_id = db.Column(db.Integer, db.ForeignKey('song_file.id'))

    def __init__(self, requester, delay, song_file_id):
        self.requester = requester
        self.delay = delay
        self.song_file_id = song_file_id


class SongFile(db.Model):

    __tablename__ = "song_file"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    youtube_id = db.Column(db.String(255), nullable=False)
    file_name = db.Column(db.String(255), nullable=True)
    percent_complete = db.Column(db.String(255), nullable=False)
    completed = db.Column(db.Boolean(), nullable=False, default=False)
    requests = db.relationship('SongRequest', backref='song')

    def __init__(self, url, title, youtube_id):
        self.url = url
        self.title = title
        self.youtube_id = youtube_id
        self.file_name = None
        self.percent_complete = "0.0%"
        self.completed = False

    def __repr__(self):
        return '<File title={} url={} youtube_key={} file_name={} percent_complete={}>'\
            .format(self.title, self.url, self.youtube_key, self.file_name, self.percent_complete)


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
