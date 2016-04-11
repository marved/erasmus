from django.forms import (
    CharField, Form
)

class LoginFormValidator(Form):
    """

    """
    username = CharField()
    password = CharField()