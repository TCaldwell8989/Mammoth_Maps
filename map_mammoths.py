import folium
from folium import plugins
import csv

# MAPS REQUIRED - BASIC MARKERS & HEATMAP

# Create map. Use terrain tiles instad of roads
mammoth_map = folium.Map(location=[40, -120], zoom_start=3, tiles="Stamen Terrain")

lat_long = []

# Read in mammoth_data.csv. Use data to create waymakers, add to map
with open('mammoth_data.csv', 'r') as mammoth_csv:
    reader = csv.reader(mammoth_csv, quoting=csv.QUOTE_NONNUMERIC)
    firstline = reader.__next__() #discard title column titles
    for line in reader:
        lat = line[3]
        long = line[4]
        lat_long.append([lat, long])
        marker_text = '%s found in %s, %s. %s.' % \
                      (line[0], line[6], line[5], line[7])
        if line[1]:
            marker_text += ' %s %s ' % (line[1], line[2])

        marker = folium.Marker([lat, long], popup=marker_text)
        marker.add_to(mammoth_map)

mammoth_map.save('mammoth_map.html')

# Heatmap, uses a list of [lat, long] coordinates

heatmap = folium.Map(location=[40, -120], zoom_start=3)
heatmap.add_children(plugins.HeatMap(lat_long))
heatmap.save('mammoth_heatmap.html')