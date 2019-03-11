#!/usr/bin/python3

from gpiozero import PWMLED
from time import sleep

led1 = PWMLED(4)
led2 = PWMLED(17)

while True:
    led1.value = 0.00
    led2.value = 0.00
    sleep(1)
    led1.value = 0.01
    led2.value = 0.01
    sleep(1)
    led1.value = 0.02
    led2.value = 0.02
    sleep(1)
    led1.value = 0.03
    led2.value = 0.03
    sleep(1)
    led1.value = 0.04
    led2.value = 0.04
    sleep(1)
    led1.value = 0.05
    led2.value = 0.05
    sleep(1)
    led1.value = 0.06
    led2.value = 0.06
    sleep(1)
    led1.value = 0.07
    led2.value = 0.07
    sleep(1)
    led1.value = 0.08
    led2.value = 0.08
    sleep(1)
    led1.value = 0.09
    led2.value = 0.09
    sleep(1)
    led1.value = 0.10
    led2.value = 0.10
    sleep(1)
    led1.value = 0.50
    led2.value = 0.50
    sleep(1)
    led1.value = 1.00
    led2.value = 1.00
