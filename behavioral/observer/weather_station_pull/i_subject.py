from abc import ABC, abstractmethod

from behavioral.observer.weather_station_pull.i_observer import IObserver


class ISubject(ABC):
    @abstractmethod
    def register_observer(self, observer: IObserver):
        raise NotImplementedError

    @abstractmethod
    def remove_observer(self, observer: IObserver):
        raise NotImplementedError

    @abstractmethod
    def notify_observer(self):
        raise NotImplementedError
