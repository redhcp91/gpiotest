#!/usr/bin/python3

from gpiozero import LEDBoard
from time import sleep
from signal import pause

leds = LEDBoard(4, 17, 27, 22)

leds[0].on() # First LED on
sleep(1)
leds[3].on() # Last LED on
sleep(1)
leds[-1].off() # Last LED off
sleep(1)
