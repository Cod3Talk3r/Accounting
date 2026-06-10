from fastapi import status, HTTPException


class NotFoundUser(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail = "User Not Found!"

    pass


class WrongUsernameOrPassword(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail = "Wrong Username Or Password!"

    pass


class ExistUsername(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_409_CONFLICT
        self.detail = "This Username Exists."

    pass


class TokenIsNotValid(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_401_UNAUTHORIZED
        self.detail = "Token is not valid!"

    pass


class UnAuthorized(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_401_UNAUTHORIZED
        self.detail = "Not Authorized!"

        pass


class NotFoundTag(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail = "Tag Not Found!"

    pass


class ExistTag(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_409_CONFLICT
        self.detail = "This Tag Exists."

    pass


class DefaultTag(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = "Can't Delete This Tag!"

    pass