"""
@author: Miguel Cabrera Ramírez <miguel.cabrera@oohel.net><mdark1001>
@project:
@date: 3/20/24
"""
import json

from rentomatic.domain import Room


class RoomJsonEncoder(json.JSONEncoder):
    def default(self,object:Room):
        try:
            to_serialize ={
                'code': str(object.code),
                'size': object.size,
                'price': float(object.price),
                'longitude': object.longitude,
                'latitude': object.latitude
            }
            return  to_serialize
        except AttributeError:
            return super().default(object)
