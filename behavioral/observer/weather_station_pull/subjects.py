
from typing import List

from behavioral.observer.weather_station_pull.i_observer import IObserver
from behavioral.observer.weather_station_pull.i_subject import ISubject


class WeatherData(ISubject):
    def __init__(self):
        self.observers: List[IObserver] = []
        self.temperature: float = 0.0
        self.humidity: float = 0.0
        self.pressure: float = 0.0

    def measurement_changed(self):
        self.notify_observer()

    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurement_changed()

    # IObserver methods:
    def register_observer(self, observer: IObserver):
        self.observers.append(observer)

    def remove_observer(self, observer: IObserver):
        self.observers.remove(observer)

    def notify_observer(self):
        for observer in self.observers:
            observer.update()
