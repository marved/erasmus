from django.forms import (
    CharField, Form
)

class LoginFormValidator(Form):
    username = CharField()
    password = CharField()

class PasswordFormValidator(Form):
    currentPassword = CharField(required=True)
    newPassword = CharField(required=True)
