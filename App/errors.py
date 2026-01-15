from fastapi import status, HTTPException


class NotFoundUser(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail = "User Not Found!"


class WrongUsernameOrPassword(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail = "Wrong Username Or Password!"


class ExistUsername(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_409_CONFLICT
        self.detail = "This Username Exists."


class ExistEmail(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_409_CONFLICT
        self.detail = "This Email Exists."
