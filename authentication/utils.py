from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import UntypedToken

from exceptions.CustomException import CustomException


def user_checking(data):
    from .models import User
    user = User.objects.filter(username=data.get('username').lower()).first()
    if not user:
        raise CustomException('User not found!')
    if check_password(data.get('password'), user.password) is False:
        raise CustomException('Password or Username incorrect!')

    return user


def identify_role(token):
    if token:
        token = token.split()[1]

        payload = UntypedToken(token)
        return payload.get('role', '')
