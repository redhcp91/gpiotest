#!/usr/bin/python3

from gpiozero import LEDBoard
from time import sleep
from signal import pause

leds = LEDBoard(4, 17, 22, 10)

leds.on()

pause()
