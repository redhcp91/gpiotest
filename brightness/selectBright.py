#!/usr/bin/python

from gpiozero import PWMLED
from time import sleep

led = PWMLED(4)

lvl = input("Input brightness (.1-1): ")

while True:
    led.value = lvl
