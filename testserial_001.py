import serial
import time
import struct

def send_serail(sn):
    ser = serial.Serial("/dev/ttyS0", baudrate=9600,timeout=3.0)
    #time.sleep(5);
    print("aaaaa")
    package = bytearray(sn)
    print(package)
    ser.write(package)

def return_serial():
    time.sleep(0.05)
    ser = serial.Serial("/dev/ttyS0", baudrate=9600,timeout=3.0)
    responsePackage = ser.read(ser.inWaiting())
    print(responsePackage)
    return responsePackage
