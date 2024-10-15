import folium
import pandas as pd 

class GPSTracker:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def plot(self):
        # Create folium map centered around the coordinates
        gpsmap = folium.map(location=self.coordinates[0], zoom_start=12)

        # add gps points to the map

        for gpsCoordinates in self.coordinates:
            folium.marker(location=gpsCoordinates).add_to(gpsmap)

        return gpsmap