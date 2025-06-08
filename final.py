##final.py
from service import WeatherService

if __name__ == "__main__":
    service = WeatherService()

    print("Weather Data ")
    print("1. Start normal service")
    print("2. Clear weather data")
    print("3. Reset entire database")

    choice = input("Select option (1-3): ")

    if choice == "1":
        service.get_latest_weather()
    elif choice == "2":
        service.clear_database()
        print("Database has been cleared")
        service.get_latest_weather()
    elif choice == "3":
        service.clear_database(full_reset=True)
        print("Database has been reset")
        service.get_latest_weather()
    else:
        print("Invalid option")
