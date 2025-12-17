import subprocess
import geopandas as gpd
import pandas as pd
import os

dirname = os.path.dirname(__file__)

lakes = gpd.read_file(dirname + '/natural_earth/ne_10m_lakes.shp')
ocean = gpd.read_file(dirname + '/natural_earth/ne_10m_ocean.shp')

lakes['water_type'] = 'lake'
ocean['water_type'] = 'ocean'

combined_gdf = pd.concat([lakes, ocean], ignore_index=True)

lakes = None
ocean = None

tippecanoe_cmd = [
    'tippecanoe',
    '-o', 'basemap.pmtiles',
    '-z5',
    '--force',
    '--layer', 'world-water' 
]

with subprocess.Popen(tippecanoe_cmd, stdin=subprocess.PIPE) as proc:
    proc.communicate(input=combined_gdf.to_json().encode('utf-8'))