#!/usr/bin/python3

from gpiozero import RGBLED
from time import sleep

led1 = RGBLED(red=4, green=17, blue=22)
led2 = RGBLED(red=5, green=13, blue=26)

led1.color = (0, 1, 0)
led2.color = (0, 1, 0)
sleep(1)
led1.color = (1, 0, 1)
led2.color = (1, 0, 1)
sleep(1)
led1.color = (1, 1, 0)
led2.color = (1, 1, 0)
sleep(1)
led1.color = (0, 1, 1)
led2.color = (0, 1, 1)
sleep(1)
led1.color = (1, 1, 1)
led2.color = (1, 1, 1)
sleep(1)
led1.color = (0, 0, 0)
led2.color = (0, 0, 0)
sleep(1)

