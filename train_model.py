import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import numpy as np

# Load the dataset with extracted features
data = np.load('models/extracted_features.npy', allow_pickle=True).item()

# Reshape the multi-dimensional arrays into 1D columns
temperature = data['temperature'].flatten()
wind_speed = data['wind_speed'].flatten()
evaporation = data['evaporation'].flatten()
runoff = data['runoff'].flatten()

# Check for NaN values and remove them
valid_indices = ~np.isnan(temperature) & ~np.isnan(wind_speed) & ~np.isnan(evaporation) & ~np.isnan(runoff)

# Keep only the valid data (without NaNs)
temperature = temperature[valid_indices]
wind_speed = wind_speed[valid_indices]
evaporation = evaporation[valid_indices]
runoff = runoff[valid_indices]

# Downsample the data to reduce the size (taking every 100th data point)
downsample_rate = 100
temperature = temperature[::downsample_rate]
wind_speed = wind_speed[::downsample_rate]
evaporation = evaporation[::downsample_rate]
runoff = runoff[::downsample_rate]

# Create a DataFrame using 1D arrays
df = pd.DataFrame({
    'temperature': temperature,
    'wind_speed': wind_speed,
    'evaporation': evaporation,
    'runoff': runoff
})

# Split data into features and target variable
X = df[['evaporation', 'wind_speed']]
y = df['temperature']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest model
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'models/saved_model.pkl')

print("Model training complete, and saved to 'models/saved_model.pkl'.")
