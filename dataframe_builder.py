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

#######################

# Create litter can dataframe
can_URL = "https://opendata.arcgis.com/datasets/4c9d7e966c0f435485fe0f47144c3258_10.geojson"

can_response = requests.get(can_URL)

can_list = []
geom_list = []

for i in range(len(can_response.json()['features'])):
    obj_id = can_response.json()['features'][i]['properties']['OBJECTID']
    rat = can_response.json()['features'][i]['properties']['RAT_COVER']
    wash = can_response.json()['features'][i]['properties']['POWERWASH']
    geom = Point(can_response.json()['features'][i]['geometry']['coordinates'])
    
    can_list.append({'object_id' : obj_id,
                     'rat_cover' : rat,
                     'power_wash' : wash})
    geom_list.append(geom)

can_df = pd.DataFrame(can_list)

litter_cans = gpd.GeoDataFrame(can_df.copy(), geometry = geom_list,)

litter_cans.to_file("data/litter_cans.shp", driver = 'ESRI Shapefile')


