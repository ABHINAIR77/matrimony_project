from .Model import Model


class User(Model):
    table = "users"
    fields = ('email', 'password', 'name','country', 'dob', 'gender', 'religion')

    def authenticate(self, login_details):
        user = self.get({"email": login_details.email})
        return True if user.password == login_details.password else False

