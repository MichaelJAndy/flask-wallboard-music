from project import db
from project.models import SongRequest, SongFile


class SongRequestDAO(object):

    def create_song_request(self, song_request):
        db.session.add(song_request)
        db.session.commit()

    def update_song_request(self, song_request):
        db.session.add(song_request)
        db.session.commit()

    def get_song_requests(self):
        return db.session.query(SongRequest).order_by(SongRequest.requester.asc()).all()

    def get_song_request_by_id(self, id):
        return db.session.query(SongRequest).filter_by(id=id).first()

    def get_song_requests_by_kwargs(self, **kwargs):
        return db.session.query(SongRequest).filter_by(**kwargs).all

    def delete_song_request(self, song_request):
        db.session.delete(song_request)
        db.session.commit()


class SongFileDAO(object):

    def create_song_file(self, song_file):
        db.session.add(song_file)
        db.session.commit()

    def update_song_file(self, song_file):
        db.session.add(song_file)
        db.session.commit()

    def get_song_files(self):
        return db.session.query(SongFile).all()

    def get_song_file_by_id(self, id):
        return db.session.query(SongFile).filter_by(id=id).first()

    def get_song_files_by_kwargs(self, **kwargs):
        return db.session.query(SongFile).filter_by(**kwargs).all()

    def get_song_file_by_youtube_id(self, youtube_id):
        return db.session.query(SongFile).filter_by(youtube_id=youtube_id).first()

    def get_song_file_by_file_name(self, file_name):
        return db.session.query(SongFile).filter_by(file_name=file_name).first()

    def delete_song_file(self, song_file):
        db.session.delete(song_file)
        db.session.commit()
