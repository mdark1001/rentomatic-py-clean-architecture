"""
@author: Miguel Cabrera Ramírez <miguel.cabrera@oohel.net><mdark1001>
@project:
@date: 3/24/24
"""
import json

from flask import Blueprint, Response, request
from rentomatic.data import room1, room2, room3
from rentomatic.repository.memrepo import MemRepo
from rentomatic.request_objects.response_objects import ResponseSuccess, ResponseFailure
from rentomatic.request_objects.room_list_request_objects import RoomListRequestObject
from rentomatic.serializers.room import RoomJsonEncoder
from rentomatic.use_cases.room_list_use_case import RoomListUseCase

blueprint = Blueprint('/rooms', __name__)

STATUS_CODES = {
    ResponseSuccess.SUCCESS: 200,
    ResponseFailure.RESOURCE_ERROR: 404,
    ResponseFailure.PARAMETERS_ERROR: 400,
    ResponseFailure.SYSTEM_ERROR: 500
}


@blueprint.route('/rooms', methods=['GET'])
def room():
    query_filters = {
        'filters':{},
    }
    for arg, value in request.args.items():
        if arg.startswith('filter_'):
            query_filters['filters'][arg.replace('filter_','')] = value

    repo = MemRepo([room1, room2, room3])
    request_object = RoomListRequestObject.from_dict(query_filters)

    use_case = RoomListUseCase(repo)

    result = use_case.execute(request_object)

    return Response(
        json.dumps(result.value, cls=RoomJsonEncoder),
        mimetype='application/json',
        status=STATUS_CODES[result.type]
    )

