#!/usr/bin/python3

from gpiozero import RGBLED
from time import sleep

led = RGBLED(red=16, green=20, blue=21)
