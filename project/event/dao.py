from project import db
from project.models import Event


class EventDAO(object):

    def create_event(self, event):
        db.session.add(event)
        db.session.commit()

    def update_event(self, event):
        db.session.add(event)
        db.session.commit()

    def get_events(self):
        return db.session.query(Event).order_by(Event.id.asc()).all()

    def get_event_by_id(self, id_number):
        return db.session.query(Event).filter_by(id=id_number).first()

    def get_events_by_kwargs(self, **kwargs):
        return db.session.query(Event).filter_by(**kwargs).all

    def delete_event(self, event):
        db.session.delete(event)
        db.session.commit()

