from gps import InterfaceGPS
from firebase_config import firebaseInit

db = firebaseInit()

gps = InterfaceGPS()
while True:
    cordenates = gps.get_position()
    db.update(cordenates)