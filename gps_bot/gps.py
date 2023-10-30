import serial
from time import sleep


class InterfaceGPS:
    def __init__(self):
        gpgga_info = "$GPGGA,"
        ser = serial.Serial ("/dev/ttyAMA0")              #Open port with baud rate
        GPGGA_buffer = 0
        NMEA_buff = 0
        received_data = (str)(ser.readline())
        GPGGA_data_available = received_data.find(gpgga_info)                
        if (GPGGA_data_available>0):
            GPGGA_buffer = received_data.split("$GPGGA,",1)[1]
            NMEA_buff = (GPGGA_buffer.split(','))
            self.latitude, self.longitude = self.GPS_Info(NMEA_buff)

    def GPS_Info(self, NMEA_buff):

        nmea_latitude = []
        nmea_longitude = []
        nmea_latitude = NMEA_buff[1]
        nmea_longitude = NMEA_buff[3]
        
        lat = float(nmea_latitude)
        longi = float(nmea_longitude)
        
        lat_in_degrees = self.convert_to_degrees(lat)
        long_in_degrees = self.convert_to_degrees(longi)
        return lat_in_degrees, long_in_degrees
    
    def convert_to_degrees(self, raw_value):
        decimal_value = raw_value/100.00
        degrees = int(decimal_value)
        mm_mmmm = (decimal_value - int(decimal_value))/0.6
        position = degrees + mm_mmmm
        position = "%.4f" % (position)
        return position

    def get_position(self):
        return self.latitude, self.longitude

while True:
    gps = InterfaceGPS()
    latitude, longitude = gps.get_position()
    print(f'Latitude:{latitude} longitude:{longitude}')