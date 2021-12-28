# from templated_mail import BaseEmailMessage
from djoser import email
# from djoser.conf import settings


class PasswordResetEmail(email.PasswordResetEmail):
    template_name = "email/password_reset_v1.html"
