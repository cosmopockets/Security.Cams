import pansas as pd
from gps_plotter.plotter import GPSTracker

def main():
    # load coordinates from data/coordinates.csv
    print("Reading coordinates from csv file")

    coords_df = pd.read_csv('data/coordinates.csv')
    coordinates = list(zip(coords_df['latitude'],coords_df['longitude']))

    # create a GPS Tracker instance and plot the coordinates
    print("Creating GPS Tracker to plot the coordinates")
    gps_tracker = GPSTracker(coordinates)
    map_object = gps_tracker.plot()

    # Save the map to an HTML file
    print("Saving map to a HTML file")
    map_object.save("gpsMap.html")
    print("Map has been created and saved")

if __name__ == "__main__":
    main()