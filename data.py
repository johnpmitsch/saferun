import pandas as pd
import ast

assault = pd.read_csv("Better assult.csv")
assault_locations = list(assault['LOCATION']) # a list of tuples
assaults = []
for location in assault_locations:
    if location is not 'NaN':
        lon, lat = ast.literal_eval(location)
        assaults.append((lon, lat))

# crashes = pd.read_csv("crashes.csv")
# crash_locations = list(crashes['coordinates']) # a list of tuples
# crash_coordinates = []
# for location in crash_locations:
#     if type(location) == float:
#         lon, lat = ast.literal_eval(location)
#         crash_coordinates.append((lon, lat))