from datetime import datetime


class WeatherModel:
    def __init__(self,city:str,temperature:float,description:str,timestamp:datetime):
        self.city=city
        self.temperature=temperature
        self.timestamp=timestamp
        self.description=description
    def __repr__(self):
        return f'{self.city}, {self.temperature}, {self.description}, {self.timestamp}'

class WeatherDTO:
    def __init__(self,city:str,temperature:float):
        self.city=city
        self.temperature=temperature
    def dictionary_conversion(self):
        return {"City":self.city,"Temperature":self.temperature}

