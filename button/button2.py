#!/usr/bin/python3

from gpiozero import LED, Button
from signal import pause

led = LED(4)
button = Button(6)

button.when_pressed = led.on
button.when_released = led.off

pause()
