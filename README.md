# CS-355-Event-Planner
 Python-Flask web app that allows users to create accounnts and schedule events

## Code Overview

The project is organized into several files:

1. `main.py`:
   - This is the main file of the Flask application.
   - It contains the routes and logic for handling user authentication, event operations, and rendering templates.
   - Database queries are made at various points in the code, specifically in the routes.

2. `forms.py`:
   - This file defines the forms used in the application.
   - There are three forms: `RegistrationForm`, `LoginForm`, and `AddEventForm`.
   - These forms validate user inputs and ensure the data entered is valid.

3. `manage.py`:
   - This script initializes the database by creating tables and adding dummy data.
   - Run `python manage.py` to set up the database.

4. `models.py`:
   - This file defines the database models using SQLAlchemy.
   - There are three models: `User`, `Event`, and `Mention`.
   - These models represent users, events, and mentions respectively.
   - Database queries are made within the models to fetch and manipulate data.

5. Templates:
   - The HTML templates are stored in the templates folder.
   - There are several templates used to render different pages of the application.
   - Templates include `base.html`, `add_event.html`, `delete_event.html`, `event_detail.html`, and `index.html`.
   - These templates provide the structure and content for the application pages.

## Database Queries

The following are the main lines in the code where database queries are made:

- `main.py`:
   - Line 18: `Event.query.order_by(...).all()`
   - Line 29: `User.query.filter_by(username=username).first()`
   - Line 44: `User.query.filter_by(username=username).first()`
   - Line 69: `Event.query.get(event_id)`
   - Line 88: `Event.query.get(event_id)`
   - Line 90: `Event.query.filter_by(user=current_user)`
   - Line 105: `Event.query.get(event_id)`
   - Line 118: `Event.query.get(event_id)`
   - Line 125: `Event.query.get(event_id)`
   - Line 134: `Event.query.filter_by(id=poster_filter)`
   - Line 153: `Event.query.join(rsvp).filter(rsvp.c.user_id == self.id)`
   - Line 162: `db.session.add(self)`
   - Line 187: `User.query.get(user_id)`

Please refer to the respective files and line numbers for a more detailed understanding of the database queries made in the application.

## Getting Started

To run the project, follow these steps:

1. Install the required dependencies by running `pip install -r requirements.txt`.
2. Set up the database by running `python manage.py`.
3. Start the Flask application by running `python main.py`.

Make sure you have Python and Flask installed on your system before running the project.

That's it! You should now be able to access and use the Event App. Feel free to explore the different features and create, RSVP, and manage events.
