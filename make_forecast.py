import numpy as np
import xarray as xr
import joblib
import pandas as pd

# Load the saved model
model = joblib.load('models/saved_model.h5')

# Load the new data from the NetCDF file
new_data = xr.open_dataset('models/6af5ed4ffe3861d6f75c007510e547eb.nc')

# Extract the same features used during training: evaporation and wind_speed
evaporation = new_data['e'].values.flatten()  # Assuming 'e' is evaporation

# Recalculate wind speed from components (u10, v10)
u10 = new_data['u10'].values.flatten()
v10 = new_data['v10'].values.flatten()
wind_speed = np.sqrt(u10**2 + v10**2)

# Create a DataFrame with only the features used during training
X_new = pd.DataFrame({
    'evaporation': evaporation,
    'wind_speed': wind_speed
})

# Predict using the loaded model
predictions = model.predict(X_new)

# Output the predictions
print("Predictions: ", predictions)
