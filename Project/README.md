Event Management System Overview:

This project is an Event Management System developed using Python and Flask framework. The system allows users to create, manage, and attend events. It provides functionality for event organizers to create and manage events, invite participants, track RSVPs, and collect feedback. Participants can browse and search for events, RSVP to attend, and provide feedback after attending.

Files and Line Numbers with Database Queries:

main.py :
Line 20: Event.query.all() - Retrieves all events from the database.
Line 32: db.session.add(event) - Adds a new event to the database.
Line 48: Event.query.get_or_404(event_id) - Retrieves an event by ID from the database.
Line 56: db.session.add(participant) - Adds a new participant to the database.
Line 80: db.session.add(feedback) - Adds new feedback to the database.
models.py :
Line 6: db.Column , Line 7: db.relationship - Defines the database models and relationships.
Line 21: db.Column , Line 22: db.Column , Line 23: db.Column - Defines the columns of the Event table.
Line 34: db.Column , Line 35: db.Column , Line 36: db.Column - Defines the columns of the Participant table.
Line 44: db.Column , Line 45: db.Column - Defines the columns of the Feedback table.
forms.py :
No direct database queries are made in this file. It defines the forms used to collect data from users.
This project demonstrates the usage of SQLAlchemy ORM for database operations instead of writing raw SQL queries. It also showcases the implementation of Flask routes, form validation, and rendering templates to create a functional event management system.