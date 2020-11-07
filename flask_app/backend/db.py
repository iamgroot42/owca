from tinydb import TinyDB, Query

import click
import os
from flask import current_app
from flask import g
from flask.cli import with_appcontext

from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta
import pandas as pd

# File import
from backend.utils import make_course_objects, make_user_objects

def get_db():
    """Connect to the application's configured database. The connection
    is unique for each request and will be reused if this is called
    again.
    """
    EXCEL_FILE_PATH = os.path.join(current_app.root_path, "data", "hci_data.xlsx")
    if "db" not in g:
        g.db = init_db(EXCEL_FILE_PATH)

    return g.db


def close_db(e=None):
    """If this request connected to the database, close the
    connection.
    """
    g.pop("db", None)
    # Nothing to do, really :3


def init_db(EXCEL_FILE_PATH):
    """Clear existing data and create new tables."""
    data = pd.read_excel(io=EXCEL_FILE_PATH, sheet_name=None,)
    
    courses = data['Courses']
    auth    = data['Authentication']
    users   = data['Users']
    assgts  = data['Assignments']
    anncts  = data['Announcements']

    course_objs = make_course_objects(courses, assgts, anncts)
    user_objs   = make_user_objects(users)
    auth_objs   = {x[0]:x[1] for x in auth.values}

    return (course_objs, user_objs, auth_objs)


def init_app(app):
    """Register database functions with the Flask app. This is called by
    the application factory.
    """
    app.teardown_appcontext(close_db)
