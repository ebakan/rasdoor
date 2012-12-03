#!/usr/bin/env python
import serial, time
arduino = serial.Serial('/dev/tty.usbmodem1411', 9600)
print "Connection successful"
arduino.flush();
arduino.write(chr(0))
arduino.flush();
arduino.write(chr(129))
arduino.flush();
print "open"
time.sleep(2)
arduino.write(chr(0))
arduino.flush();
print "closed"
