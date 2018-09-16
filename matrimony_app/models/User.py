from .Model import Model
from pprint import pprint as pp

class User(Model):
    table = "users"
    fields = ('id', 'email', 'password', 'name','country', 'dob', 'gender', 'religion')

    def authenticate(self, login_details):
        user = self.get({"email": login_details["email"]})
        return True if hasattr(user, "password") and user.password == login_details["password"] else False

