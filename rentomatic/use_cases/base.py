"""
@author: Miguel Cabrera Ramírez <miguel.cabrera@oohel.net><mdark1001>
@project:
@date: 3/20/24
"""
from abc import ABC, abstractmethod




class BaseUseCase(ABC):

    @abstractmethod
    def execute(self):
        raise NotImplementedError
