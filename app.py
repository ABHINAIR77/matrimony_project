from flask import Flask
from flask import render_template,request, redirect,url_for
from flask_mysqldb import MySQL

import json

app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'matrimony'

mysql = MySQL(app)

@app.route('/')
def hello_world():
    cur = mysql.connection.cursor()

    cur.execute('''
        insert into users values(2, "abhijith@test.com", "pwd1", "abhijith")  
    ''')

    cur.execute('''SELECT * FROM users''')
    rv = cur.fetchall()
    mysql.connection.commit()
    return json.dumps(rv)


@app.route('/login', methods=['GET', 'POST'])
def login(name=None):
    if request.method == "POST":
        # if username and password is equal to arjun redirect to home page
        # else redirect to login page
        print(request.form['username'] == "arjun")
        if request.form['username'] == "arjun" and request.form['password'] == "password":
            return redirect(url_for("home"))
        else:
            return redirect(url_for("login"))
    return render_template('login.html', name=name)


@app.route('/home')
def home():
    return "welcome to home page"


@app.route("/register", methods=['GET', 'POST'])
def register():
    return user.UserController().register()
