import re
import testserial_001 as ser

def Picture(group, number): # Fix at 8,9
    sn = [255, 1, 8, 1, 0, 0, 0, 0, group, number, 0, 0, 0, 0, 0]
    print(sn)
    ser.send_serail(sn)
    #sn2 = int.from_bytes(sn, byteorder='big', signed=False)
    #print(sn2)

def RFID_card():
    #try:
        #responsePackage = ser.return_serial()
        #response = True
    #except:
        #group = None
        #number = None
    rsp = [255, 1, 50, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 9]
    robotmode = rsp[2]
    reply = rsp[3]
    kick = rsp[4]
    group = rsp[14]
    number = rsp[15]
    return robotmode, reply, kick, group, number

def RFID_activity():
    # responsePackage = ser.return_serial()
    rsp = [255, 1, 50, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 9]
    mode = rsp[14]
    number = rsp[15]
    return mode,number


if __name__ == '__main__':
    RFID_card()
