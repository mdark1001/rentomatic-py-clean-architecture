"""
@author: Miguel Cabrera Ramírez <miguel.cabrera@oohel.net><mdark1001>
@project:
@date: 3/25/24
@description: Request and response objects are an important part of a clean architecture
they transport call parameters, input and results from outside the application into the use cases layer.
"""
from  collections.abc import Mapping
from typing_extensions import Self

from rentomatic.request_objects.base import BaseRequestObject
from rentomatic.request_objects.response_objects import InvalidRequestObject


class RoomListRequestObject(BaseRequestObject):
    accepted_filters = ['code__eq', 'price__eq', 'price__lt', 'price__gt']

    def __init__(self, filters=None) -> None:
        self.filters = filters

    @classmethod
    def from_dict(cls, adict: dict )-> Self:
        invalid_request_object = InvalidRequestObject()
        if 'filters' in adict:
            if not isinstance(adict['filters'], Mapping):
                invalid_request_object.add_error('filters', 'Is not an iterable')
                return invalid_request_object
            for key, value in adict['filters'].items():
                if key not in cls.accepted_filters:
                    invalid_request_object.add_error(
                        'filters', f'Key "{key}" is not an accepted'
                    )
        if invalid_request_object.has_errors():
            return invalid_request_object

        return cls(
            filters=adict.get('filters', None)
        )

    def __bool__(self):
        return True


