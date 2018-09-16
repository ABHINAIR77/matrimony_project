from flask import g


def init_app(app):
    app.teardown_appcontext(close_db)


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.connection.close()


