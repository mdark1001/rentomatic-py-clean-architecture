"""
@author: Miguel Cabrera Ramírez <mdark1001>
@project:
@date: 3/19/24
"""

import uuid

from rentomatic.domain.room import Room



def test_room_model_init():
    code = uuid.uuid4()
    my_room = Room(
        code=code,
        size=200,
        price=10,
        longitude=0.0991223,
        latitude=51.89128
    )
    assert my_room.code == code
    assert my_room.size == 200
    assert my_room.price == 10
    assert my_room.longitude == 0.0991223
    assert my_room.latitude == 51.89128


def test_room_model_from_dict():
    code = uuid.uuid4()
    my_room = Room.from_dict({
        'code': code,
        'size': 200,
        'price': 10,
        'longitude': 0.0991223,
        'latitude': 51.89128,
    })

    assert my_room.code == code
    assert my_room.size == 200
    assert my_room.price == 10
    assert my_room.longitude == 0.0991223
    assert my_room.latitude == 51.89128


def test_room_model_repr():
    code = uuid.uuid4()
    my_room = Room.from_dict({
        'code': code,
        'size': 200,
        'price': 10,
        'longitude': 0.0991223,
        'latitude': 51.89128,
    })
    assert repr(my_room) == 'Room(code={})'.format(code)


def test_room_model_to_dict_method():
    code = uuid.uuid4()
    data = {
        'code': code,
        'size': 200,
        'price': 10,
        'longitude': 0.0991223,
        'latitude': 51.89128,
    }
    my_room = Room.from_dict(data)
    assert my_room.to_dict() == data


def test_room_model_eq_method():
    code = uuid.uuid4()
    data = {
        'code': code,
        'size': 200,
        'price': 10,
        'longitude': 0.0991223,
        'latitude': 51.89128,
    }
    my_room = Room.from_dict(data)
    my_room2 = Room.from_dict(data)
    assert my_room == my_room2


