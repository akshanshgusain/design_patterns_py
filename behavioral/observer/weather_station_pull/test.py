from behavioral.observer.weather_station_pull.observers import CurrentConditionsDisplay
from behavioral.observer.weather_station_pull.subjects import WeatherData

if __name__ == "__main__":
    weather_data: WeatherData = WeatherData()
    current_display: CurrentConditionsDisplay = CurrentConditionsDisplay(weather_data)

    weather_data.set_measurements(80, 65, 30.5)
    weather_data.set_measurements(83, 60, 31.5)
    weather_data.set_measurements(86, 57, 30.5)