# Event App Readme

This is a Flask web application that allows users to register, log in, and organize events. Users can add events, RSVP to events, view event details, and delete events. The application uses a SQLite database to store user information and event data.

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

To run the project, you will need to follow these steps:

Install Python: Make sure you have Python installed on your system.

Install Flask: Open your terminal and run the command pip install flask to install the Flask framework.

Install SQLAlchemy: Run the command pip install sqlalchemy to install the SQLAlchemy library for database operations.

Create a virtual environment (optional): It is recommended to create a virtual environment for this project. Run the command python -m venv venv to create a virtual environment named venv (you can use any name).

Activate the virtual environment: Activate the virtual environment by running the appropriate command for your operating system.

For Windows: venv\Scripts\activate
For macOS/Linux: source venv/bin/activate
Set up the database: In the main.py file, you will find the line app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///event_management.db' . This configures the application to use an SQLite database file named event_management.db . Make sure you have SQLite installed on your system.

Run the application: Execute the command python main.py to start the Flask development server. The application will be accessible at http://localhost:5000 in your web browser.

## Notes

Couldn't quite get event deletion and event filtering functionality up and running but the logic is in the code.
