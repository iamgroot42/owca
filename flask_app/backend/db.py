from tinydb import TinyDB, Query

import click
import os
from flask import current_app
from flask import g
from flask.cli import with_appcontext

def get_db():
    """Connect to the application's configured database. The connection
    is unique for each request and will be reused if this is called
    again.
    """
    # Should be global, figure out later
    DATASET_PATH = os.path.join(current_app.root_path, "data", "db.json")
    if "db" not in g:
        g.db = TinyDB(DATASET_PATH)

    return g.db


def close_db(e=None):
    """If this request connected to the database, close the
    connection.
    """
    db = g.pop("db", None)

    if db is not None:
        db.close()


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
    DATASET_PATH = os.path.join(current_app.root_path, "data", "db.json")

    with open(DATASET_PATH, 'w') as fp:
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
    pass
