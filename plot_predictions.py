import pandas as pd
import matplotlib.pyplot as plt

# Load predictions
data = pd.read_csv("glof_predictions.csv", parse_dates=["timestamp"])

# Plot water level & risk level
plt.figure(figsize=(8, 5))

# Plot water level
plt.plot(data["timestamp"], data["water_level_m"], marker="o", linestyle="-", color="blue", label="Water Level (m)")

# Highlight high-risk points
high_risk = data[data["GLOF_Risk"] == 1]
plt.scatter(high_risk["timestamp"], high_risk["water_level_m"], color="red", label="High Risk ⚠️", s=100, edgecolors="black")

# Formatting the plot
plt.xlabel("Time")
plt.ylabel("Water Level (m)")
plt.title("GLOF Risk Prediction")
plt.xticks(rotation=45)
plt.legend()
plt.grid()

# Show the plot
plt.show()
