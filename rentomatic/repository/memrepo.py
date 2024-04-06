"""
@author: Miguel Cabrera Ramírez <miguel.cabrera@oohel.net><mdark1001>
@project:
@date: 3/22/24
"""
from decimal import Decimal

from rentomatic.domain import Room


class MemRepo:

    def __init__(self, data):
        self.data = data

    def list(self, filters=None):
        result = [Room.from_dict(d) for d in self.data]
        if not filters:
            return result
        if 'code__eq' in filters:
            result = [r for r in result if r.code == filters['code__eq']]
        if 'price__eq' in filters:
            result = [r for r in result if r.price == Decimal(filters['price__eq'])]
        if 'price__lt' in filters:
            result = [r for r in result if r.price < Decimal(filters['price__lt'])]
        if 'price__gt' in filters:
            result = [r for r in result if r.price > Decimal(filters['price__gt'])]
        return result
