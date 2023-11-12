from gps import InterfaceGPS

gps = InterfaceGPS()
while True:
    cordenates = gps.get_position()
