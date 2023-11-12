import serial
from time import sleep


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
            coordenates = {"latitude":float(latitude), "longitude" :float(longitude)}
            self.write_data(coordenates)
            return coordenates

    def write_data(self, data):
        with open("/var/wwww/html/data.txt", "w") as file:
            file.write(data)

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
        position = "%.4f" % (position)
        return position
