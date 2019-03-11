#!/usr/bin/python

from gpiozero import LED
from time import sleep

led4 = LED(4)
led17 = LED(17) 

while True:
    led4.on()
    led17.on()
