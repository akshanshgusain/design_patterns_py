from abc import ABC, abstractmethod


class IObserver(ABC):
    @abstractmethod
    def update(self, temp: float, humidity: float, pressure: float):
        raise NotImplementedError
