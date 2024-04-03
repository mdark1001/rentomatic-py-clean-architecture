"""
@author: Miguel Cabrera Ramírez <miguel.cabrera@oohel.net><mdark1001>
@project:
@date: 3/20/24
"""

from rentomatic.request_objects.base import BaseRequestObject
from rentomatic.request_objects.response_objects import ResponseSuccess, ResponseFailure

from rentomatic.use_cases.base import BaseUseCase


class RoomListUseCase(BaseUseCase):
    def __init__(self, repository):
        self._repository = repository

    def execute(self, request: BaseRequestObject):
        if not request:
            return ResponseFailure.build_from_invalid_request(request)
        try:

            rooms = self._repository.list(filters=request.filters)
            return ResponseSuccess(rooms)
        except Exception as ee:
            return ResponseFailure.build_system_error(
                "{}: {}".format(ee.__class__.__name__, "{}".format(ee)))
