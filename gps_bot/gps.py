import serial
from time import sleep


def GPS_Info():

    nmea_latitude = []
    nmea_longitude = []
    nmea_latitude = NMEA_buff[1]
    nmea_longitude = NMEA_buff[3]
    
    lat = float(nmea_latitude)
    longi = float(nmea_longitude)
    
    lat_in_degrees = convert_to_degrees(lat)
    long_in_degrees = convert_to_degrees(longi)
    return lat_in_degrees, long_in_degrees
    
#convert raw NMEA string into degree decimal format   
def convert_to_degrees(raw_value):
    decimal_value = raw_value/100.00
    degrees = int(decimal_value)
    mm_mmmm = (decimal_value - int(decimal_value))/0.6
    position = degrees + mm_mmmm
    position = "%.4f" %(position)
    return position


gpgga_info = "$GPGGA,"
ser = serial.Serial ("/dev/ttyAMA0")              #Open port with baud rate
GPGGA_buffer = 0
NMEA_buff = 0

while True:
    received_data = (str)(ser.readline())                   #read NMEA string received
    GPGGA_data_available = received_data.find(gpgga_info)   #check for NMEA GPGGA string                 
    if (GPGGA_data_available>0):
        GPGGA_buffer = received_data.split("$GPGGA,",1)[1]  #store data coming after "$GPGGA," string 
        NMEA_buff = (GPGGA_buffer.split(','))               #store comma separated data in buffer
        lattitude, longuitud = GPS_Info()                                          #get time, latitude, longitude

        print("lat in degrees:", lattitude," long in degree: ", longuitud, '\n')

