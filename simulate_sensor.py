import random
import time
import json
import sqlite3

# Simulating real-time water level sensor data
def generate_water_level():
    base_level = 3.0  # Initial water level in meters

    # Connect to the database
    conn = sqlite3.connect("glof_data.db")
    cursor = conn.cursor()

    while True:
        fluctuation = random.uniform(-0.2, 0.5)  # Random increase/decrease
        base_level = max(2.5, base_level + fluctuation)  # Prevent very low values
        
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        water_level = round(base_level, 2)

        # Store in the database
        cursor.execute("INSERT INTO sensor_data (timestamp, water_level_m) VALUES (?, ?)", 
                       (timestamp, water_level))
        conn.commit()

        print(f"✅ Data saved: {timestamp}, Water Level: {water_level}m")
        time.sleep(5)  # Update every 5 seconds

# Run the simulation
if __name__ == "__main__":
    generate_water_level()
