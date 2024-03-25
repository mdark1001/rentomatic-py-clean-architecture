"""
@author: Miguel Cabrera Ramírez <miguel.cabrera@oohel.net><mdark1001>
@project:
@date: 3/22/24
"""
from rentomatic.domain import Room


class MemRepo:

    def __init__(self,data):
        self.data = data
    def list(self):
        return [Room.from_dict(d) for d in self.data]
