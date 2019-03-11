#!/usr/bin/python3

from gpiozero import LEDBarGraph, CPUTemperature
from time import sleep
from signal import pause

#graph = LEDBarGraph(4, 17, 22, 10)
cpu = CPUTemperature(min_temp=50, max_temp=80)
leds = LEDBarGraph(4, 17, 22, 10, pwm=True)

leds.source = cpu

pause()

#graph.value = 1
#sleep(1)
#graph.value = 1/2
#sleep(1)
#graph.value = -1/2
#sleep(1)
#graph.value = 1/4
#sleep(1)
#graph.value = -1
#sleep(1)
