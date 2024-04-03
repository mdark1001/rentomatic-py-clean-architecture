"""
@author: Miguel Cabrera Ramírez <miguel.cabrera@oohel.net><mdark1001>
@project:
@date: 3/24/24
"""
import json
import logging
from unittest import mock
from rentomatic.domain.room import Room
from rentomatic.request_objects.response_objects import ResponseSuccess

room1 = {
    'code': 'f853578c-fc0f-4e65-81b8-566c5dffa35a',
    'size': 215,
    'price': 39.0,
    'longitude': -0.09998975,
    'latitude': 51.75436293,
}

room = Room.from_dict(room1)
rooms = [room]


@mock.patch('rentomatic.use_cases.room_list_use_case.RoomListUseCase')
def test_get_rooms_list(mock_use_case, client):
    """
    Test the get_rooms_list.
    Client: it is a fixture that is automatically load by pytest-flask. It's an object to simulate an HTTP
    client that can access the API endpoints and store responses of the server.
    """
    ## logging.info(mock_use_case.execute)
    mock_use_case().execute.return_value = ResponseSuccess(rooms)

    http_response = client.get('/rooms')
    assert json.loads(http_response.data.decode('UTF-8')) == [room1]
    # mock_use_case.assert_called_with()
    mock_use_case().execute.assert_called

    args, kwargs = mock_use_case.call_args
    print(args,kwargs)
    assert args[0].filters == {}

    assert http_response.status_code == 200
    assert http_response.mimetype == 'application/json'
