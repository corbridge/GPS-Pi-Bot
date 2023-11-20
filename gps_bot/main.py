from gps import InterfaceGPS
from motors import Direction

gps = InterfaceGPS()
direction = Direction()

destination_lat = None
destination_lng = None

while True:
    cordenates = gps.get_position()
    gps.sending_data_js(cordenates)

    distance = gps.distanceBetween(cordenates['latitude'], cordenates['longitude'],destination_lat, destination_lng)
    angle = gps.course_to(cordenates['latitude'], cordenates['longitude'],destination_lat, destination_lng)

    if angle == 0:
        if distance <= 0:
            direction.neutral()
        else:
            direction.foward()
    else:
        direction.neutral()
        print(f'Ajuste el vehiculo {angle} grados')