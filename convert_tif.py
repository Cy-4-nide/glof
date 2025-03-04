import pandas as pd
import matplotlib.pyplot as plt

# Load sensor data
sensor_data = pd.read_csv("sensor_data.csv", parse_dates=["timestamp"])

# Plot water level over time
plt.figure(figsize=(8, 4))
plt.plot(sensor_data["timestamp"], sensor_data["water_level_m"], marker="o", linestyle="-", color="b", label="Water Level (m)")
plt.xlabel("Time")
plt.ylabel("Water Level (m)")
plt.title("Water Level Trends")
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.show()
