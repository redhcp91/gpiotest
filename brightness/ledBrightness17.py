#!/usr/bin/python

from gpiozero import PWMLED
from time import sleep

led = PWMLED(17)

while True:
    led.value = 0 # off
    sleep(1)
    led.value = 0.5 # 50% brightness
    sleep(1)
    led.value = 1 # 100% brightness
    sleep(1)
