from gps import InterfaceGPS
from motors import Direction

gps = InterfaceGPS()
direction = Direction()

#lat1, lon1 = 25.7423252, -100.2794307  # Mty
lat2, lon2 = 25.7422753, -100.2794433  # san Nico

while True:
    cordenates = gps.get_position()
    gps.sending_data_js(cordenates)

    distance = gps.distanceBetween(cordenates['latitude'], cordenates['longitude'],lat2, lon2)
    angle = gps.course_to(cordenates['latitude'], cordenates['longitude'],lat2, lon2)

    # if angle == 0:
    if distance <= 0:
        #direction.neutral()
        print(f'La distancia es: {distance}')
    else:
        #direction.foward()
        print(f'La distancia es: {distance}')
    # else:
#        direction.neutral()
        # print(f'Ajuste el vehiculo {angle} grados')