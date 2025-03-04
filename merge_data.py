import pandas as pd

# Load sensor and weather data
sensor_data = pd.read_csv("sensor_data.csv", parse_dates=["timestamp"])
weather_data = pd.read_csv("weather_data.csv", parse_dates=["timestamp"])

# Merge datasets on timestamp
combined_data = pd.merge(sensor_data, weather_data, on="timestamp")

# Save the merged dataset
combined_data.to_csv("merged_data.csv", index=False)

# Display first few rows
print(combined_data.head())
