from gui import GPSGui
from gps import InterfaceGPS

gps = InterfaceGPS()
while True:
    latitude, longitude = gps.get_position()
    GPSGui(latitude, longitude)