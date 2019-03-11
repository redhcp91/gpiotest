#!/usr/bin/python3

from gpiozero import LED, Button
from signal import pause

led1 = LED(5)
button1 = Button(26)

button1.when_pressed = led1.on
button1.when_released = led1.off

pause()
