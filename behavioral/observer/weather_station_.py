from abc import ABC, abstractmethod
from typing import List


class IObserver(ABC):
    @abstractmethod
    def update(self, temp: float, humidity: float, pressure: float):
        raise NotImplementedError


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


# make the WeatherData class implement ISubject interface
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
            observer.update(self.temperature, self.humidity, self.pressure)


class IDisplayElement(ABC):
    @abstractmethod
    def display(self):
        raise NotImplementedError


# Display Monitors - Observers
class CurrentConditionsDisplay(IObserver, IDisplayElement):
    def __init__(self, weather_data: WeatherData):
        self.temperature: float = 0.0
        self.humidity: float = 0.0
        self.weather_data: WeatherData = weather_data
        self.weather_data.register_observer(self)

    # interface methods
    def update(self, temp: float, humidity: float, pressure: float):
        self.temperature = temp
        self.humidity = humidity
        self.display()

    def display(self):
        print(f"Current conditions: {self.temperature} degrees and {self.humidity}% humidity")


if __name__ == "__main__":
    weather_data: WeatherData = WeatherData()
    current_display: CurrentConditionsDisplay = CurrentConditionsDisplay(weather_data)

    weather_data.set_measurements(80, 65, 30.5)
    weather_data.set_measurements(83, 60, 31.5)
    weather_data.set_measurements(86, 57, 30.5)
