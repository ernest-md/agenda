import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

# Aquest document recull els metodes necesaris per accedir a la base dades que utilitza l'aplicació

# metode per accedir a la base de dades


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


# metode per tancar l'acces a la base de dades
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


# metode que arranca la base de dades
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


# metode que crea el comand 'init-db' que al fer 'flask init-db' en la shell, arranca la base de dades
@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
