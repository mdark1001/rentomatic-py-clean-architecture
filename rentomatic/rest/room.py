"""
@author: Miguel Cabrera Ramírez <miguel.cabrera@oohel.net><mdark1001>
@project:
@date: 3/24/24
"""
import json

from flask import Blueprint, Response
from rentomatic.data import room1, room2, room3
from rentomatic.repository.memrepo import MemRepo
from rentomatic.serializers.room import RoomJsonEncoder
from rentomatic.use_cases.room_list_use_case import RoomListUseCase

blueprint = Blueprint('/rooms', __name__)


@blueprint.route('/rooms', methods=['GET'])
def room():
    repo = MemRepo([room1, room2, room3])
    use_case = RoomListUseCase(repo)
    result = use_case.execute()

    return Response(
        json.dumps(result, cls=RoomJsonEncoder),

        mimetype='application/json',
        status=200
    )
