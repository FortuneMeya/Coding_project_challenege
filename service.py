"""
Author: Fortune Meya
Date:06/08/2025
Backend
Main service that helps tie everything together
"""
from datetime import datetime
import time
from config import CITIES,UPDATE
from api import WeatherApi
from models import WeatherModel
from repository import WeatherRepository


class WeatherService:
    def __init__(self, api=None, repo=None):
        """
        Used to pass mock versions for testing
        :param api:  the api instance
        :param repo: the repository instance
        """
        self.api = api or WeatherApi()
        self.repo = repo or WeatherRepository()
    def update_weather(self,city):
        """
        Gets the freshest weather for the city and saves it
        :param city: the city name
        """
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
        """
        Main loop that runs forever by getting the updates
        :return:
        """
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
        """
        Cleans our the old data
        :param full_reset:whether to clear the database or not
        :return:
        """
        if full_reset:
            self.repo.reset_database()
        else:
            self.repo.clear_all_data()


