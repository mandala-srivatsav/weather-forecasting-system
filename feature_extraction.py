import xarray as xr
import numpy as np

# Load the processed NetCDF data file
data_path = "models/6af5ed4ffe3861d6f75c007510e547eb.nc"
data = xr.open_dataset(data_path)

# Extract the desired features (example: temperature, wind speed, etc.)
# Modify these variables based on the ones present in your dataset

# Example: Extracting temperature ('t2m'), which is in Kelvin
temperature = data['t2m'].values  # t2m is typically temperature at 2 meters

# Extract wind speed ('u10' and 'v10' for horizontal and vertical wind components)
u10 = data['u10'].values  # U-component of wind at 10 meters
v10 = data['v10'].values  # V-component of wind at 10 meters

# Calculate wind speed from its components
wind_speed = np.sqrt(u10**2 + v10**2)

# Example: Extracting total evaporation ('e') and runoff ('ro')
evaporation = data['e'].values
runoff = data['ro'].values

# Add more feature extraction logic as per your dataset

# Save the extracted features to a NumPy file (structured as a dictionary)
extracted_features = {
    'temperature': temperature,
    'wind_speed': wind_speed,
    'evaporation': evaporation,
    'runoff': runoff
}

# Save the features in 'models/extracted_features.npy'
np.save("models/extracted_features.npy", extracted_features)

print("Feature extraction complete. Features saved to 'models/extracted_features.npy'.")
