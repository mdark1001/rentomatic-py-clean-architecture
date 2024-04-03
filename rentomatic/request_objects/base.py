"""
@author: Miguel Cabrera Ramírez <miguel.cabrera@oohel.net><mdark1001>
@project:
@date: 3/25/24
"""
import abc


class BaseRequestObject(abc.ABC):
    @classmethod
    def from_dict(cls, adict):
        return NotImplementedError

    def __bool__(self):
        return True

    def get_errors(self):
        ...
