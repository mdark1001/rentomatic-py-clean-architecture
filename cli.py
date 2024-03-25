#!/usr/bin/env python
"""
@author: Miguel Cabrera Ramírez <miguel.cabrera@oohel.net><mdark1001>
@project:
@date: 3/22/24
"""
from rentomatic.data import room1, room2, room3
from rentomatic.repository.memrepo import MemRepo
from rentomatic.use_cases.room_list_use_case import RoomListUseCase


repository = MemRepo([room1, room2, room3])

use_case = RoomListUseCase(repository)
result = use_case.execute()

print([room.to_dict() for room in result])
