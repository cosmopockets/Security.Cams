import unittest
from gps_plotter.plotter import GPSTracker

class TestGPSTracker(unittest.TestCase):
    def test_plot(self):
        gpsCoords = [(37.80585857440136,-122.21764223076121), (37.80592426934864,-122.2185944149615), (37.86846365835632,-122.29001725344962)]
        gps_tracker = GPSTracker(gpsCoords)
        map_object = gps_tracker.plot()

        # A check to see if the map was created
        self.assertIsNotNone(map_object)

if __name__ == '__main__':
    unittest.main()