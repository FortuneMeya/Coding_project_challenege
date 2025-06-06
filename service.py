from datetime import datetime

from api import WeatherApi
from models import WeatherModel
from repository import WeatherRepository


class WeatherService:
    def __init__(self):
        self.api = WeatherApi()
        self.repo= WeatherRepository()
    def update_weather(self,city):
        data= self.api.fetch_current(city)

        forecast = data['list'][0]
        temperature = forecast['main']['temp']
        description = forecast['weather'][0]['description']
        timestamp = forecast['dt']
        timestamp = datetime.fromtimestamp(forecast['dt'])

        weather= WeatherModel(
            city=city,
            temperature=temperature,
            description=description,
            timestamp=timestamp,
        )
        self.repo.save(weather)
    def get_latest_weather(self,city):
        return self.repo.get_by_city(city)

