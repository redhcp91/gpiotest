#!/usr/bin/python

#from signal import pause
from gpiozero import Button

tFile = open('/sys/class/thermal/thermal_zone0/temp')
temp = float(tFile.read())
tempC = temp/1000

button1 = Button(10)

button1.wait_for_press()
print(tempC)

