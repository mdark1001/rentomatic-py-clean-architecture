"""
@author: Miguel Cabrera Ramírez <miguel.cabrera@oohel.net><mdark1001>
@project:
@date: 3/25/24
"""
import pytest

from rentomatic.request_objects.room_list_request_objects import RoomListRequestObject


def test_room_list_request_objects_no_params():
    request = RoomListRequestObject()
    assert request.filters is None
    assert bool(request) is True


def test_build_room_list_request_objects_from_empty_dict():
    request = RoomListRequestObject.from_dict({})
    assert request.filters is None
    assert bool(request) is True


def test_build_room_list_request_with_empty_filters():
    request = RoomListRequestObject(filters={})

    assert request.filters == {}
    assert bool(request) is True


def test_build_room_list_request_object_from_dict_with_empty_filters():
    request = RoomListRequestObject.from_dict({'filters': {}})
    assert request.filters == {}
    assert bool(request) is True


def test_build_room_list_request_object_from_dict_with_filters_wrong():
    request = RoomListRequestObject.from_dict({'filters': {'a': 1}})
    assert request.has_errors()
    assert request._errors[0]['parameter'] == 'filters'
    assert bool(request) is False


def test_build_room_list_request_object_from_dict_with_invalid_filters():
    request = RoomListRequestObject.from_dict({'filters': 5})
    assert request.has_errors()
    assert request._errors[0]['parameter'] == 'filters'
    assert bool(request) is False


@pytest.mark.parametrize(
    'key', ['code__eq', 'price__eq', 'price__lt', 'price__gt']
)
def test_build_room_list_request_object_accepted_filters(key):
    filters = {key: 1}
    request = RoomListRequestObject.from_dict({'filters': filters})
    assert request.filters == filters
    assert bool(request) is True


@pytest.mark.parametrize(
    'key',
    ['code__lt', 'code__gt']
)
def test_build_room_list_request_object_rejected_filters(key):
    """
    pytest.mark.parametrize decorator to run the same test on multiple value,
     the accepted filters
    """
    filters = {key: 1}
    request = RoomListRequestObject.from_dict({'filters': filters})
    assert request.has_errors()
    assert request._errors[0]['parameter'] == 'filters'
    assert bool(request) is False
