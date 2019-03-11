#!/usr/bin/python

from gpiozero import PWMLED
from time import sleep

led4 = PWMLED(4)
led17 = PWMLED(17)
led22 = PWMLED(22)

while True:
    led4.value = 0 # off
    sleep(1)
    led4.value = 0.5 # 50% brightness
    sleep(1)
    led4.value = 1 # 100% brightness
    sleep(1)
