from gui import GPSGui
from gps import InterfaceGPS

gps = InterfaceGPS()
while True:
    cordenates = gps.get_position()
    # GPSGui(latitude, longitude)