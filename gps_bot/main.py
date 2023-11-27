from gps import InterfaceGPS
from motors import Direction
from firebase import firebaseInit

db = firebaseInit()
gps = InterfaceGPS()
direction = Direction()

lat2, lon2 = 25.73369, -100.30064

while True:
    cordenates = gps.get_position()
    if cordenates is not None:
        db.update(cordenates)

        distance = gps.distanceBetween(cordenates['latitude'], cordenates['longitude'],lat2, lon2)
        angle = gps.course_to(cordenates['latitude'], cordenates['longitude'],lat2, lon2)

        if distance < 3:
            direction.neutral()
            break
        else:
            direction.foward()
