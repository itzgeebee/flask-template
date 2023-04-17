import pyodbc
import re

import click
from flask import current_app, g


def get_db():
    if 'db' not in g:
        server = current_app.config['DATABASE_HOST']
        database = current_app.config['DATABASE']
        username = current_app.config['DATABASE_USER']
        password = current_app.config['DATABASE_PASSWORD']
        print(
            database
        )
        g.db = pyodbc.connect(
            'DRIVER={ODBC Driver 18 for SQL Server};SERVER='
            + server + ';DATABASE='
            + database + ';UID=' +
            username + ';PWD=' + password)

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.cursor().execute(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
