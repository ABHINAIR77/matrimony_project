import os
from flask import Flask, g
from flask_mysqldb import MySQL
from pprint import pprint as pp

def create_app(test_config = None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route("/register", methods=['GET', 'POST'])
    def register():
        from matrimony_app.controller.user_controller import UserController
        return UserController().register()

    @app.route("/login", methods = ["GET","POST"])
    def login():
        from matrimony_app.controller.user_controller import UserController
        return UserController().login()

    from . import db
    with app.app_context():
        app.db = MySQL(app)
    db.init_app(app)

    return app