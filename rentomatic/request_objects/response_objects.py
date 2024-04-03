"""
@author: Miguel Cabrera Ramírez <miguel.cabrera@oohel.net><mdark1001>
@project:
@date: 4/2/24
"""
from typing_extensions import Self

from rentomatic.request_objects.base import BaseRequestObject


class InvalidRequestObject(BaseRequestObject):
    def __init__(self):
        self._errors = []

    def add_error(self, parameter: str, message: str):
        self._errors.append({'parameter': parameter, 'message': message})

    def has_errors(self) -> bool:
        return len(self._errors) > 0

    def get_errors(self) -> list:
        return self._errors

    def __bool__(self):
        return False


class ResponseSuccess:
    SUCCESS ='Success'

    def __init__(self, value=None):
        self.type = self.SUCCESS
        self.value = value

    def __bool__(self):
        return True


class ResponseFailure:
    RESOURCE_ERROR = 'ResourceError'
    PARAMETERS_ERROR = 'ParametersError'
    SYSTEM_ERROR = 'SystemError'

    def __init__(self, type, message: str | Exception):
        self.type = type
        self.message = self._format_message(message)

    def _format_message(self, message: str | Exception) -> str:
        if isinstance(message, Exception):
            return "{}: {}".format(message.__class__.__name__, "{}".format(message))
        return str(message)

    @property
    def value(self):
        return {'type': self.type, 'message': self.message}

    def __bool__(self):
        return False

    @classmethod
    def build_from_invalid_request(cls, invalid_request: BaseRequestObject) -> Self:
        messages = "\n".join([
            "{}: {}".format(err['parameter'], err['message'])
            for err in invalid_request.get_errors()
        ])
        return cls(cls.PARAMETERS_ERROR, message=messages)

    @classmethod
    def build_resource_error(cls, message: str = "") -> Self:
        return cls(cls.RESOURCE_ERROR, message)

    @classmethod
    def build_system_error(cls, message: str = ""):
        return cls(cls.SYSTEM_ERROR, message)

    @classmethod
    def build_parameters_error(cls, message: str = ""):
        return cls(cls.PARAMETERS_ERROR, message)
