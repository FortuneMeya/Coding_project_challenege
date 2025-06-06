from service import WeatherService

def main():
    service = WeatherService()
    cities= ['Los Angeles','Miami','Milan','Chicago']
    for city in cities:
        try:
            service.update_weather(city)
            print(f'{city} updated')
        except Exception as e:
            print(f'Failed to update {city}: {e}')

    for city in cities:
        data= service.get_latest_weather(city)
        if data:
            print(f'{data.city}: {data.temperature},{data.description} at {data.timestamp}')
        else:
            print(f'{city} has no data')

main()