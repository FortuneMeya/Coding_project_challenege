Weather Data Collector

This is a Python project that collects weather data for a few cities and saves it to a database.

Run the program:
python final.py

When it starts, you'll see a menu:

Press 1 to start collecting weather data (runs forever)

Press 2 to clear all the saved weather data

Press 3 to completely reset everything

The program checks weather every 30 minutes for:

Los Angeles

Miami

Milan

Chicago

All the data gets saved to a file called temp.db in the same folder.

That's it! The code is split up into different files so it's easier to work with:

api.py - talks to the weather service

models.py - how we store weather data

repository.py - saves data to the database

service.py - the main logic

config.py - settings you can change


ALL WORK DONE BY FORTUNE MEYA :)
