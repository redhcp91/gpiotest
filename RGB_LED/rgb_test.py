#!/usr/bin/python3

from gpiozero import RGBLED
from time import sleep

led = RGBLED(red=4, green=17, blue=22)

led.red = 1
sleep(1)
led.red = 0.5
sleep(1)

led.color = (0, 1, 0) # full green
sleep(1)
led.color = (1, 0, 1) # magenta
sleep(1)
led.color = (1, 1, 0) # yellow
sleep(1)
led.color = (0, 1, 1) # cyan
sleep(1)
led.color = (1, 1, 1) # white
sleep(1)

led.color = (0, 0, 0,) # off
sleep(1)

# slowly increase intensity of blue
for n in range(100):
    led.blue = n/100
    sleep(0.1)