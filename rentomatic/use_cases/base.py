"""
@author: Miguel Cabrera Ramírez <miguel.cabrera@oohel.net><mdark1001>
@project:
@date: 3/20/24
"""
from abc import ABC, abstractmethod
from rentomatic.request_objects.base import BaseRequestObject

class BaseUseCase(ABC):

    @abstractmethod
    def execute(self, request:BaseRequestObject):
        raise NotImplementedError
