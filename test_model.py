import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler

# Load the trained model
model = load_model("glof_risk_model.h5")

# Load the merged dataset (for testing)
data = pd.read_csv("merged_data.csv")

# Select input features
X = data[["water_level_m", "temperature_c_x", "flow_rate_m3s", "temperature_c_y", "rainfall_mm"]]

# Normalize input data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Make predictions
predictions = model.predict(X_scaled)
risk_levels = (predictions > 0.5).astype(int)

# Add predictions to dataset
data["GLOF_Risk"] = risk_levels

# Save results
data.to_csv("glof_predictions.csv", index=False)

# Print results
print(data[["timestamp", "water_level_m", "rainfall_mm", "GLOF_Risk"]])
print("\n✅ Prediction complete! Results saved in 'glof_predictions.csv'")
