import xarray as xr

# Correct path to the .nc file
data = xr.open_dataset("D:/4-1/MAJOR_PROJECT/weather_forecasting_backend/models/6af5ed4ffe3861d6f75c007510e547eb.nc")
print(data)
