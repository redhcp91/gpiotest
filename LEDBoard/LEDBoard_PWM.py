#!/usr/bin/python3

from gpiozero import LEDBoard
from signal import pause

leds = LEDBoard(4, 17, 22, pwm=True)

leds.value = (0.1, 0.2, 1.0)

pause()
