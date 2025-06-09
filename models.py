"""
Author: Fortune Meya
Date:06/08/2025
Backend
Tests for the weather service
Holds information about a city's weather
"""

from datetime import datetime


class WeatherModel:
    def __init__(self,city:str,temperature:float,description:str,timestamp:datetime):
        """

        :param city: The name of the city
        :type city: str
        :param temperature: The temperature of the city
        :type temperature: float
        :param description: The description of the city
        :type description: str
        :param timestamp: The timestamp of the city
        :type timestamp: datetime

        """
        self.city=city
        self.temperature=temperature
        self.timestamp=timestamp
        self.description=description

    def __str__(self):
        """
        Creates a one line summary of the weather information
        :return: Returns a string representation of the weather model
        """
        return f'{self.city}: {self.temperature}, {self.description} at {self.timestamp:%Y-%m-%d %H:%M}'
