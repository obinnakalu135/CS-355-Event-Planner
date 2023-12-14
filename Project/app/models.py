from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    mentions = db.relationship('Mention', backref='user', lazy=True)
    rsvps = db.relationship('Event', secondary='rsvp', backref='attendees', lazy='dynamic')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def get_events_attending(self):
        return Event.query.join(rsvp).filter(rsvp.c.user_id == self.id)

    @staticmethod
    def get(user_id):
        return User.query.get(user_id)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    date = db.Column(db.Date, nullable=False)
    organizer = db.Column(db.String(128), nullable=False)
    location = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)


class Mention(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


rsvp = db.Table('rsvp',
                db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True))
