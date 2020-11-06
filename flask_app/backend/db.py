from tinydb import TinyDB, Query

import click
import os
from flask import current_app
from flask import g
from flask.cli import with_appcontext

from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta

def get_db():
    """Connect to the application's configured database. The connection
    is unique for each request and will be reused if this is called
    again.
    """
    # Should be global, figure out later
    USER_DATA_PATH   = os.path.join(current_app.root_path, "data", "users.json")
    COURSE_DATA_PATH = os.path.join(current_app.root_path, "data", "courses.json")
    if "db" not in g:
        userdb   = TinyDB(USER_DATA_PATH)
        coursedb = TinyDB(COURSE_DATA_PATH)
        g.db = (userdb, coursedb)

    return g.db


def close_db(e=None):
    """If this request connected to the database, close the
    connection.
    """
    db = g.pop("db", None)
    if db is not None:
        (userdb, coursedb) = db

        if userdb is not None:
            userdb.close()
    
        if coursedb is not None:
            coursedb.close()


def init_db():
    """Clear existing data and create new tables."""
    db = get_db()

    # Populate with data (dummy for now)
    populate_dummy_data(db)


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    # Should be global, figure out later
    USER_DATA_PATH   = os.path.join(current_app.root_path, "data", "users.json")
    COURSE_DATA_PATH = os.path.join(current_app.root_path, "data", "courses.json")

    with open(USER_DATA_PATH, 'w') as _:
        pass

    with open(COURSE_DATA_PATH, 'w') as _:
        pass

    init_db()
    click.echo("Initialized the database.")


def init_app(app):
    """Register database functions with the Flask app. This is called by
    the application factory.
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def populate_dummy_data(db):
    userdb, coursedb = db

    # Dummy users
    userdb.insert({"id": "potato",
        "password": generate_password_hash("potato"),
        "courses": ["hci"]})
    userdb.insert({"id": "tomato",
        "password": generate_password_hash("tomato"),
        "courses": []})
    userdb.insert({"id": "avocado",
        "password": generate_password_hash("avocado"),
        "courses": []})

    # Dummy courses
    coursedb.insert({"id": "hci",
                    "instructor": "tomato",
                    "tas": ["avocado"],
                    "session": (2020, "fall"),
                    "description": "dummy HCI course go brr",
                    "assignments": [
                        {
                            "name": "Reading Response 10: Based on Topic Presentation List T11/T12",
                            "description": "Reading response for Nov 11 topic presentations. Choose one from the following four papers:",
                            "due_date": (datetime.now() + timedelta(days=5)).strftime("%Y-%m-%d, %H:%M:%S"),
                            "assignment_link": "https://collab.its.virginia.edu/portal/site/b69a0900-b4b4-41de-b8c2-21a864b70229/tool/c2e78b95-f0ab-4b6a-a6f3-c0d67ff7924d?panel=Main"
                        },
                        {
                            "name": "Reading Response 9: Based on Topic Presentation List T9/T10",
                            "description": "Reading response for Nov 9 topic presentations. Choose one from the following four papers:",
                            "due_date": (datetime.now() + timedelta(hours=2)).strftime("%Y-%m-%d, %H:%M:%S"),
                            "assignment_link": "https://collab.its.virginia.edu/portal/site/b69a0900-b4b4-41de-b8c2-21a864b70229/tool/c2e78b95-f0ab-4b6a-a6f3-c0d67ff7924d?panel=Main"
                        },
                        {
                            "name": "Project Progress Report",
                            "description": "Please submit your project progress report (PDF) following one of the CHI proceeding formats:",
                            "due_date": (datetime.now() - timedelta(days=15)).strftime("%Y-%m-%d, %H:%M:%S"),
                            "assignment_link": "https://collab.its.virginia.edu/portal/site/b69a0900-b4b4-41de-b8c2-21a864b70229/tool/c2e78b95-f0ab-4b6a-a6f3-c0d67ff7924d?panel=Main"
                        },
                        {
                            "name": "Dummy overflow assignment",
                            "description": "SHOW ME WHAT YOU GOT!!",
                            "due_date": (datetime.now() + timedelta(days=3, minutes=45)).strftime("%Y-%m-%d, %H:%M:%S"),
                            "assignment_link": "https://reddit.com"
                        },
                        {
                            "name": "Dummy overflow assignment",
                            "description": "SHOW ME WHAT YOU GOT!!",
                            "due_date": (datetime.now() + timedelta(days=5, minutes=35)).strftime("%Y-%m-%d, %H:%M:%S"),
                            "assignment_link": "https://reddit.com"
                        },
                        {
                            "name": "Dummy overflow assignment",
                            "description": "SHOW ME WHAT YOU GOT!!",
                            "due_date": (datetime.now() + timedelta(days=2, minutes=5)).strftime("%Y-%m-%d, %H:%M:%S"),
                            "assignment_link": "https://reddit.com"
                        },
                        ],
                    "meetings": [("now", "BRR JOIN google.com")],
                    "annoucements": [("haha", "hehe")]})
