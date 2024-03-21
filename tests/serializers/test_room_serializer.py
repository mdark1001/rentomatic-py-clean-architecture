"""
@author: Miguel Cabrera Ramírez <miguel.cabrera@oohel.net><mdark1001>
@project:
@date: 3/20/24
"""
import json
import logging
import uuid

from rentomatic.domain import Room
from rentomatic.serializers.room import RoomJsonEncoder


def test_serializer_room_domain_model():
    code = uuid.uuid4()
    data = {
        'code': code,
        'size': 200,
        'price': 10,
        'longitude': -0.09998975,
        'latitude': 51.75436293,
    }
    my_room = Room.from_dict(data)
    expected_json = f"""
           {{
               "code": "{code}",
               "size": 200,
               "price": 10.0,
               "longitude": -0.09998975,
               "latitude": 51.75436293
           }}
       """

    json_room = json.dumps(my_room, cls=RoomJsonEncoder)

    assert json.loads(json_room) == json.loads(expected_json)
