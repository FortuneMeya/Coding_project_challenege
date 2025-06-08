import sqlite3
from datetime import datetime

from models import WeatherModel
class WeatherRepository:
    def __init__(self,db_path='temp.db'):
        self.conn = sqlite3.connect(db_path)
        self._create_table()
    def _create_table(self):
        with self.conn:
            self.conn.execute("""
            CREATE TABLE IF NOT EXISTS data_numbers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL,
            temperature REAL,
            description TEXT,
            timestamp TEXT

);
                              """)

    def save(self, weather: WeatherModel):
        with self.conn:
            self.conn.execute("""
                              INSERT INTO data_numbers (city, temperature, description, timestamp)
                              VALUES (?, ?, ?, ?)
                              """, (
                                  weather.city,
                                  weather.temperature,
                                  weather.description,
                                  # Replace this line:
                                  weather.timestamp.strftime('%Y-%m-%d %H:%M:%S')  # Removes the 'T'
                              ))
            self.conn.commit()

    def get_by_city(self, city: str):
        cur = self.conn.cursor()
        cur.execute("""
                    SELECT city, temperature, description, timestamp
                    FROM data_numbers
                    WHERE city = ?
                    ORDER BY timestamp DESC
                    LIMIT 1
                    """, (city,))
        row = cur.fetchone()
        if row:
            try:
                timestamp = datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
            except ValueError:
                timestamp = datetime.fromisoformat(row[3])
            return WeatherModel(row[0], row[1], row[2], timestamp)
        return None

    def clear_all_data(self):
        with self.conn:
            self.conn.execute("DELETE FROM data_numbers")
            self.conn.commit()
        print("All weather data cleared from database")

    def reset_database(self):
        with self.conn:
            self.conn.execute("DROP TABLE IF EXISTS data_numbers")
            self._create_table()
        print("Database completely reset")


