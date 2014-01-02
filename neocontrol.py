#!/usr/bin/env python

import serial

usbport = '/dev/ttyACM1'

ser = serial.Serial(usbport, 9600, timeout=1)



def strand_mode(mode):
    ser.write(chr(255))
    ser.write(chr(mode))
    ser.write(chr(0))

def setPixelColor(num, red, green, blue):
    ser.write(chr(255))
    ser.write(chr(4))
    ser.write(chr(num))
    ser.write(chr(red))
    ser.write(chr(green))
    ser.write(chr(blue))


