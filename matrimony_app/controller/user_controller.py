from flask import render_template, request, redirect, url_for
from pprint import pprint as pp
from matrimony_app.models.User import User


class UserController:
    def register(self):
        if request.method == 'GET':
            return render_template('register.html')
        elif request.method == 'POST':
            form_dict = request.form.to_dict()
            user = User()
            user.create(form_dict)
            return redirect(url_for('register'))


    def login(self):
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            user = User()
            login_details = request.form.to_dict()
            if user.authenticate(login_details):
                # @todo redirect to home page
                return "Login Successful"
            else:
                return redirect(url_for("login"))


