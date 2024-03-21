"""
@author: Miguel Cabrera Ramírez <miguel.cabrera@oohel.net><mdark1001>
@project:
@date: 3/19/24
"""
import dataclasses
from decimal import Decimal


class Room:
    code: str
    size: int
    price: Decimal
    longitude: float
    latitude: float

    def __init__(self, code: str, size: int, price: Decimal, longitude: float, latitude: float):
        self.code = code
        self.size = size
        self.price = price
        self.longitude = longitude
        self.latitude = latitude

    @classmethod
    def from_dict(cls, data: dict) -> 'Room':
        return cls(
            code=data['code'],
            size=data['size'],
            price=Decimal(data['price']),
            longitude=float(data['longitude']),
            latitude=float(data['latitude']),
        )

    def to_dict(self) -> dict:
        return {
            'code': self.code,
            'size': self.size,
            'price': self.price,
            'longitude': self.longitude,
            'latitude': self.latitude,
        }

    def __repr__(self) -> str:
        return "Room(code={})".format(self.code)

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()
