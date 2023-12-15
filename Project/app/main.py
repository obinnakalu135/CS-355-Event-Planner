from flask import Flask, render_template, flash, redirect, url_for, session, request
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash


from models import db, User, Event, Mention
from forms import LoginForm, RegistrationForm, AddEventForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///event_management.db'
db.init_app(app)


login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
   return User.get(user_id)


@app.route('/')
def index():
  sort_by = request.args.get('sort_by', 'recent')  # Get the sorting option from the query string
  events = Event.query.order_by(Event.date.desc() if sort_by == 'recent' else Event.date.asc()).all()
  form = AddEventForm()  # Add this line
  return render_template('index.html', events=events, form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
   form = RegistrationForm()
   if form.validate_on_submit():
       username = form.username.data
       password = form.password.data


       existing_user = User.query.filter_by(username=username).first()
       if existing_user:
           flash('Username already exists.')
           return redirect(url_for('register'))


       user = User(username=username, password=generate_password_hash(password))
       user.save()
       flash('Registration successful. Please log in.')
       return redirect(url_for('login'))


   return render_template('register.html', form=form)




@app.route('/login', methods=['GET', 'POST'])
def login():
   form = LoginForm()
   if form.validate_on_submit():
       username = form.username.data
       password = form.password.data


       user = User.query.filter_by(username=username).first()
       if user and check_password_hash(user.password, password):
           login_user(user)
           return redirect(url_for('index'))
       flash('Invalid username or password.')


   return render_template('login.html', form=form)




@app.route('/logout')
@login_required
def logout():
   logout_user()
   flash('You have been logged out.')
   return redirect(url_for('index'))




@app.route('/add_event', methods=['GET', 'POST'])
@login_required
def add_event():
  form = AddEventForm()
  if form.validate_on_submit():
      name = form.name.data
      date = form.date.data
      organizer = form.organizer.data
      location = form.location.data
      description = form.description.data


      event = Event(name=name, date=date, organizer=organizer, location=location, description=description)
      db.session.add(event)  # Save the event to the database
      db.session.commit()  # Commit the changes
      flash('Event added successfully.')
      return redirect(url_for('index'))


  return render_template('add_event.html', form=form)


@app.route('/event/<int:event_id>/', methods=['GET', 'POST'])
@login_required
def event_detail(event_id):
    event = Event.query.get(event_id)
    form = AddEventForm()

    if form.validate_on_submit():
        current_user.rsvps.append(event)
        db.session.commit()  # Commit the changes to the rsvps relationship
        flash('You have successfully RSVPed.')

    return render_template('event_detail.html', event=event, form=form)


@app.route('/rsvp/<int:event_id>/', methods=['POST'])
@login_required
def rsvp(event_id):
    event = Event.query.get(event_id)
    current_user.rsvps.append(event)
    db.session.commit()
    flash('You have successfully RSVPed.')
    return redirect(url_for('event_detail', event_id=event.id))


@app.errorhandler(404)
def page_not_found(e):
   return render_template('404.html'), 404

@app.route('/delete_event/<int:event_id>', methods=['POST'])
@login_required
def delete_event(event_id):
  event = Event.query.get(event_id)
  if event:
      if event.user == current_user:  # Check if the event belongs to the current user
          db.session.delete(event)
          db.session.commit()
          flash('Event deleted successfully.')
      else:
          flash('You are not authorized to delete this event.')
  else:
      flash('Event not found.')
  return redirect(url_for('index'))


@app.route('/events/filter')
def filter_events():
  date_filter = request.args.get('date')
  poster_filter = request.args.get('poster')
  location_filter = request.args.get('location')
  events_query = Event.query

  if date_filter:
      events_query = events_query.filter_by(date=date_filter)

  if poster_filter:
      events_query = events_query.join(Event.user).filter_by(id=poster_filter)

  if location_filter:
      events_query = events_query.filter_by(location=location_filter)

  events = events_query.all()
  form = AddEventForm()
  return render_template('index.html', events=events, form=form)

if __name__ == '__main__':
   app.run(debug=True)
