#!/usr/bin/env python
import serial, time
try:
    arduino = serial.Serial('/dev/tty.usbmodem1411', 9600)
    print "Connection successful"
    val = int(input())
    #arduino.write(chr(val))
    arduino.write(chr(180));
    arduino.flush();
    time.sleep(2);
    arduino.write(chr(0));
    arduino.flush();
except:
    print "Connection failed"
