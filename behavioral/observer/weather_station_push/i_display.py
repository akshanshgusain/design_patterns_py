from abc import ABC, abstractmethod


class IDisplayElement(ABC):
    @abstractmethod
    def display(self):
        raise NotImplementedError
