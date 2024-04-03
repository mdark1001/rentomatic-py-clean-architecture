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
from rentomatic.request_objects.response_objects import ResponseFailure
from rentomatic.request_objects.room_list_request_objects import RoomListRequestObject
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
    # adding request object
    request = RoomListRequestObject()

    result = room_list_use_case.execute(request)
    assert bool(result) is True

    repo.list.assert_called_with(filters=None)

    assert result.value == domain_rooms


def test_room_list_with_filters(domain_rooms):
    repo = mock.Mock()
    repo.list.return_value = domain_rooms
    room_list_use_case = RoomListUseCase(repository=repo)
    qry_filters = {'code__eq': 5}
    request_object = RoomListRequestObject.from_dict({'filters': qry_filters})
    response_object = room_list_use_case.execute(request_object)
    assert bool(response_object) is True
    repo.list.assert_called_with(filters=qry_filters)
    assert response_object.value == domain_rooms


def test_room_list_handles_generic_error():
    repo = mock.Mock()
    repo.list.side_effect = Exception('Just an error message')
    room_list_use_case = RoomListUseCase(repo)
    request_object = RoomListRequestObject.from_dict({})
    response_object = room_list_use_case.execute(request_object)
    assert bool(response_object) is False
    assert response_object.value == {
        'type': ResponseFailure.SYSTEM_ERROR,
        'message': "Exception: Just an error message"
    }
def test_room_list_handles_bad_request():
    repo = mock.Mock()
    room_list_use_case = RoomListUseCase(repo)
    request_object = RoomListRequestObject.from_dict({'filters': 5})
    response_object = room_list_use_case.execute(request_object)
    assert bool(response_object) is False
    assert response_object.value == {
        'type': ResponseFailure.PARAMETERS_ERROR,
        'message': "filters: Is not an iterable"
    }
