import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load merged dataset
data = pd.read_csv("merged_data.csv")

# Select input features (X) and target variable (Y)
X = data[["water_level_m", "temperature_c_x", "flow_rate_m3s", "temperature_c_y", "rainfall_mm"]]
Y = (data["water_level_m"] > 5.5).astype(int)  # 1 if high risk, 0 if low risk

# Split data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Normalize the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Build the neural network model
model = keras.Sequential([
    keras.layers.Dense(16, activation="relu", input_shape=(X_train.shape[1],)),
    keras.layers.Dense(8, activation="relu"),
    keras.layers.Dense(1, activation="sigmoid")
])

# Compile the model
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Train the model
model.fit(X_train_scaled, Y_train, epochs=50, batch_size=4, validation_data=(X_test_scaled, Y_test))

# Save the model
model.save("glof_risk_model.h5")

print("✅ Model training complete and saved as 'glof_risk_model.h5'!")
