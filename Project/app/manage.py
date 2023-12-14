from main import db, app
from models import User, Event, Mention
from forms import AddEventForm


if __name__ == '__main__':
   with app.app_context():
       db.create_all()
       
       # Add some dummy data to test the application
       user = User(username='admin', password='admin')
       event = Event(name='Test Event', date='2021-01-01', organizer='Organizer', location='Location', description='Description')
       user.rsvps.append(event)
       db.session.add(user)
       db.session.commit()