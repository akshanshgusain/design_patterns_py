from abc import ABC, abstractmethod

"""
Command is behavioral design pattern that converts requests or simple operations into objects.
"""

"""
Command pattern encapsulates a request as an object, thereby letting you parameterize other objects with
different requests, queue or log requests and support undoable operations.
"""


#  Abstract base command

class ICommand(ABC):

    @abstractmethod
    def execute(self) -> bool:
        pass

