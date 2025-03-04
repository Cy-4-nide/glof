import requests
import json
import sqlite3
import time

# OpenWeather API Key (Replace with your actual key)
API_KEY = "3f690ae551a31b26e6f55173dfff9c42"
CITY = "Kathmandu"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def get_weather():
    try:
        response = requests.get(URL)
        data = response.json()
        
        if response.status_code == 200:
            weather_info = {
                "temperature_c": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "rainfall_mm": data.get("rain", {}).get("1h", 0)
            }
            return weather_info
        else:
            print("Error:", data["message"])
            return None

    except Exception as e:
        print("Failed to fetch weather data:", e)
        return None

# Store in the database
def save_weather_data():
    conn = sqlite3.connect("glof_data.db")
    cursor = conn.cursor()

    while True:
        weather = get_weather()
        if weather:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("INSERT INTO sensor_data (timestamp, temperature_c, humidity, rainfall_mm) VALUES (?, ?, ?, ?)", 
                           (timestamp, weather["temperature_c"], weather["humidity"], weather["rainfall_mm"]))
            conn.commit()
            print(f"✅ Weather data saved: {timestamp}, Temp: {weather['temperature_c']}°C, Humidity: {weather['humidity']}%, Rainfall: {weather['rainfall_mm']}mm")

        time.sleep(10)  # Fetch weather data every 10 seconds

if __name__ == "__main__":
    save_weather_data()
