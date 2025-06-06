import sqlite3

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
    def save(self,weather:WeatherModel):
        with self.conn:
            self.conn.execute("""
            INSERT INTO data_numbers (city, temperature, description, timestamp)
            VALUES (?, ?, ?, ?)
        """, (weather.city, weather.temperature, weather.description, weather.timestamp))

    def get_by_city(self,city:str):
        cur = self.conn.cursor()
        cur.execute("""
                    SELECT city, temperature, description, timestamp
                    FROM data_numbers WHERE city =? ORDER BY timestamp DESC LIMIT 1
        """, (city,))
        row = cur.fetchone()
        if row:
            return WeatherModel(*row)
        return None


