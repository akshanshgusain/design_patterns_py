# Display Monitors - Observers
from behavioral.observer.weather_station_pull.i_display import IDisplayElement
from behavioral.observer.weather_station_pull.i_observer import IObserver
from behavioral.observer.weather_station_pull.subjects import WeatherData


class CurrentConditionsDisplay(IObserver, IDisplayElement):
    def __init__(self, weather_data: WeatherData):
        self.temperature: float = 0.0
        self.humidity: float = 0.0
        # subject: weather data
        self.weather_data: WeatherData = weather_data
        self.weather_data.register_observer(self)

    # interface methods
    def update(self):
        self.temperature = self.weather_data.temperature
        self.humidity = self.weather_data.humidity
        self.display()

    def display(self):
        print(f"Current conditions: {self.temperature} degrees and {self.humidity}% humidity")