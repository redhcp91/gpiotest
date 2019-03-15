#!/usr/bin/python3

from gpiozero import LEDBarGraph, CPUTemperature
from signal import pause

cpu = CPUTemperature(min_temp=40, max_temp=90)
leds = LEDBarGraph(4, 17, 27, 22, 10, pwm=True)

leds.source = cpu

pause()
