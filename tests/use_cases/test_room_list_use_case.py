"""
@author: Miguel Cabrera Ramírez <miguel.cabrera@oohel.net><mdark1001>
@project:
@date: 3/20/24
"""
import random

import pytest
import uuid
from unittest import mock
from rentomatic.domain.room import Room
from rentomatic.use_cases.room_list_use_case import RoomListUseCase


@pytest.fixture
def domain_rooms() -> list[Room]:
    return [
        Room.from_dict(
            {
                'code': uuid.uuid4(),
                'size': random.randint(0, 500),
                'price': random.random() * 100,
                'longitude': -92.12134,
                'latitude': 54.1412,
            }
        )
        for _ in range(10)
    ]


def test_room_list_without_parameters(domain_rooms):
    repo = mock.Mock()
    repo.list.return_value = domain_rooms
    room_list_use_case = RoomListUseCase(repository=repo)
    result = room_list_use_case.execute()
    repo.list.assert_called_with()
    assert result == domain_rooms
