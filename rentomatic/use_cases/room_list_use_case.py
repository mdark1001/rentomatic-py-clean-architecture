"""
@author: Miguel Cabrera Ramírez <miguel.cabrera@oohel.net><mdark1001>
@project:
@date: 3/20/24
"""
from rentomatic.use_cases.base import BaseUseCase


class RoomListUseCase(BaseUseCase):
    def __init__(self, repository):
        self._repository = repository

    def execute(self):
        return self._repository.list()

