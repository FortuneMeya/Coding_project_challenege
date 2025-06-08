from datetime import datetime, timezone
import time
from config import CITIES,UPDATE
from api import WeatherApi
from models import WeatherModel
from repository import WeatherRepository


class WeatherService:
    def __init__(self, api=None, repo=None):
        self.api = api or WeatherApi()
        self.repo = repo or WeatherRepository()
    def update_weather(self,city):
        print(f"Checking weather for {city}")
        data= self.api.fetch_current(city)
        if data:
            timestamp = datetime.fromtimestamp(data["time"])
            weather = WeatherModel(
                city=city,
                temperature=data["temp"],
                description=data["desc"],
                timestamp=timestamp
            )
            self.repo.save(weather)
            print(f"Updated weather for {city}")
    def get_latest_weather(self):
        print(f"Will update every {UPDATE} minutes")
        while True:
            try:
                for city in CITIES:
                    self.update_weather(city)
                time.sleep(UPDATE*60)
            except KeyboardInterrupt:
                print("Exiting service")
                break
            except Exception as e:
                print(f"Error: {e}")
                time.sleep(60)

    def clear_database(self, full_reset=False):
        if full_reset:
            self.repo.reset_database()
        else:
            self.repo.clear_all_data()


