import serial
from math import radians, sin, cos, sqrt, atan2, degrees, pi

class InterfaceGPS:
    def __init__(self):
        self.gpgga_info = "$GPGGA,"
        self.ser = serial.Serial ("/dev/ttyAMA0")
        self.GPGGA_buffer = 0
        self.NMEA_buff = 0

    def get_position(self):
        try:
            received_data = str(self.ser.readline())
        except serial.serialutil.SerialException:
            print("No data received")
        GPGGA_data_available = received_data.find(self.gpgga_info)                
        if (GPGGA_data_available>0):
            self.GPGGA_buffer = received_data.split("$GPGGA,",1)[1]
            self.NMEA_buff = (self.GPGGA_buffer.split(','))
            latitude, longitude = self.GPS_Info(self.NMEA_buff)
            coordenates = {'latitude':float(latitude), 'longitude' :float(longitude)}
            if coordenates is None:
                pass
            else:
                return coordenates

    def sending_data_js(self, data):
        if data is not None:
            print(data)
            with open("/var/www/html/data.js",'w') as file:
                file.write(f"let latitude =  {str(data['latitude'])};\n")
                file.write(f"let longitude = {str(data['longitude'])};\n")
        else:
            pass

    def GPS_Info(self, NMEA_buff):
        nmea_latitude = []
        nmea_longitude = []
        nmea_latitude = NMEA_buff[1]
        nmea_longitude = NMEA_buff[3]
        
        lat = float(nmea_latitude)
        longi = float(nmea_longitude)
        
        lat_in_degrees = self.convert_to_degrees(lat)
        long_in_degrees = self.convert_to_degrees(longi * -1)
        return lat_in_degrees, long_in_degrees
    
    def convert_to_degrees(self, raw_value):
        decimal_value = raw_value/100.00
        degrees = int(decimal_value)
        mm_mmmm = (decimal_value - int(decimal_value))/0.6
        position = degrees + mm_mmmm
        position = "%.5f" % (position)
        return position

    def distanceBetween(self, origin_lat, origin_long, dest_lat, dest_long):
        # Earth Radious (km)
        R = 6371.0

        origin_lat, origin_long, dest_lat, dest_long = map(radians, [origin_lat, origin_long, dest_lat, dest_long])

        dlat = dest_lat - origin_lat
        dlon = dest_long - origin_long

        # Haversine Formula
        a = sin(dlat / 2)**2 + cos(origin_lat) * cos(dest_lat) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c

        return distance /1000 #meters

    def course_to(self, origin_lat, origin_long, dest_lat, dest_long):
        dlon = radians(dest_long - origin_long)

        origin_lat, dest_lat = radians(origin_lat), radians(dest_lat)

        a1 = sin(dlon) * cos(dest_lat)
        a2 = sin(origin_lat) * cos(dest_lat) * cos(dlon)
        a2 = cos(origin_lat) * sin(dest_lat) - a2

        # Azimuthal angle
        azimuth = atan2(a1, a2)
        azimuth = (azimuth + 2 * pi) % (2 * pi)

        return degrees(azimuth)