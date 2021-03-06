class AMSException(Exception):
    def __init__(self, code, errorType, message):
        self.code = code
        self.type = errorType
        self.message = message


class BadRequestException(AMSException):

    def __init__(self, message="The request is invalid, missing information, or out of context."):
        self.code = 400
        self.type = "BadRequest"
        self.message = message


class UnauthorizedException(AMSException):

    def __init__(self, message="The Authorization header is either missing, invalid, or expired."):
        self.code = 401
        self.type = "UnauthorizedRequest"
        self.message = message


class ForbiddenException(AMSException):

    def __init__(self, message="The request is valid but was refused."):
        self.code = 403
        self.type = "ForbiddenRequest"
        self.message = message


class NotFoundException(AMSException):

    def __init__(self, message="The requested resource could not be found."):
        self.code = 404
        self.type = "NotFound"
        self.message = message


class ClientException(AMSException):

    def __init__(self, message="The request was refused per out rate limiting policy."):
        self.code = 429
        self.type = "ClientError"
        self.message = message


class InternalException(AMSException):

    def __init__(self, message="Well, this is embarrassing... Something went wrong on our end. Please contact jake@PROJECT_NAME.com."):
        self.code = 500
        self.type = "InternalError"
        self.message = message
