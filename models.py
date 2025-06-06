from datetime import datetime


class WeatherModel:
    def __init__(self,city:str,temperature:float,time:datetime):
        self.city=city
        self.temperature=temperature
        self.time=time
class WeatherDTO:
    def __init__(self,city:str,temperature:float):
        self.city=city
        self.temperature=temperature
    def dictionary_conversion(self):
        return {"City":self.city,"Temperature":self.temperature}

