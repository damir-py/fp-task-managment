from rest_framework.exceptions import APIException
from rest_framework import status


class CustomException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(self, detail=None):
        self.detail = {'message': detail, 'ok': False}
