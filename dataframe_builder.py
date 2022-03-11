# -*- coding: utf-8 -*-
'''
Data Collection through opendata.dc.gov api
'''

# libraries
import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon, Point
import requests

#######################

# Create DC boundary shape file
DC_Tile_URL = "https://opendata.arcgis.com/datasets/cea539444b484a5e9034fa3442e2e69a_0.geojson"
DC_response = requests.get(DC_Tile_URL)


city = DC_response.json()['features'][0]['properties']['CITY_NAME']
state = DC_response.json()['features'][0]['properties']['STATE_NAME']
area = DC_response.json()['features'][0]['properties']['AREAKM']

geom = Polygon(DC_response.json()['features'][0]['geometry']['coordinates'][0])

DC_shape = gpd.GeoDataFrame({'city_name': city,
                             'state_name': state,
                             'area_km': area},
                            geometry = [geom],
                            index = [0])

# write to .shp
DC_shape.to_file("data/DC_boundary.shp", driver = 'ESRI Shapefile')



