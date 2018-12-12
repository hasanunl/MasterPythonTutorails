#Import Library
import folium
from folium.plugins import MarkerCluster
import pandas as pd
import json

#Load Data
state_data = pd.read_csv("us-unemployment.csv")
state_geo = json.load(open("us-states.json"))
state = data['State']
unemp = data['Unemployment']


map = folium.Map(location=[37.296933,-121.9574983], zoom_start = 8, tiles = "CartoDB dark_matter")

map.choropleth(geo_data=state_geo,
    name='choropleth',
    data=state_data,
    columns=['State', 'Unemployment'],
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Unemployment Rate (%)')

#Save the map
map.save("map1.html")