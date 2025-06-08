import logging

import requests
from config import API_KEY
import aiohttp


class ProjectException(Exception):
    pass


class WeatherApi:
    def __init__(self):
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        self.api_key = API_KEY

    def fetch_current(self, city: str):
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'
            }
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            return {
                'temp': data['main']['temp'],
                'desc': data['weather'][0]['description'],
                'time': data['dt']
            }
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            raise ProjectException("API has Failed") from e





