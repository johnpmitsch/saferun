import pandas as pd
import ast

assault = pd.read_csv("Assault.csv")
assault_locations = list(assault['LOCATION']) # a list of tuples
assaults = []
for location in assault_locations:
    if type(location) == str:
        lon, lat = ast.literal_eval(location)
        assaults.append((lon, lat))

