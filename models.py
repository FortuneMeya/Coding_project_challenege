from datetime import datetime


class WeatherModel:
    def __init__(self,city:str,temperature:float,description:str,timestamp:datetime):
        self.city=city
        self.temperature=temperature
        self.timestamp=timestamp
        self.description=description

    def __str__(self):
        return f'{self.city}: {self.temperature}, {self.description} at {self.timestamp:%Y-%m-%d %H:%M}'
