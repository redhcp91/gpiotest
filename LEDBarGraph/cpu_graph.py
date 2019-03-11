#!/usr/bin/python3

from gpiozero import LEDBarGraph, CPUTemperature
from signal import pause

cpu = CPUTemperature(min_temp=40, max_temp=90)
leds = LEDBarGraph(4, 17, 22, 5, 6, 13, 19, 26,  pwm=True)

leds.source = cpu

pause()
