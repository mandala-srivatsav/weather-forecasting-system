import cdsapi

dataset = "reanalysis-era5-land"
request = {
    'variable': ['2m_temperature', 'lake_bottom_temperature', 'snow_depth', 'snowfall', 'volumetric_soil_water_layer_1', 'volumetric_soil_water_layer_2', 'surface_net_solar_radiation', 'surface_net_thermal_radiation', 'runoff', 'total_evaporation', '10m_u_component_of_wind', '10m_v_component_of_wind', 'leaf_area_index_high_vegetation'],
    'year': '2024',
    'month': '08',
    'day': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
    'time': ['06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00'],
    'data_format': 'netcdf',
    'download_format': 'unarchived',
    'area': [36, 67, 4, 98]
}

client = cdsapi.Client()
client.retrieve(dataset, request).download()
