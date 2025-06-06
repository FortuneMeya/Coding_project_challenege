import logging

import requests


class ProjectException(Exception):
    pass


class WeatherApi:
    def __init__(self):
        self.key='d50a79125f0672c539cebad1f255b1bf'
    def fetch_current(self, city:str):
     try:

        url=f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={self.key}&units=metric'
        response=requests.get(url)
        response.raise_for_status()
        return response.json()
     except Exception as e:
          logging.error(f"Error occurred: {e}")
          raise ProjectException("API has Failed") from e







