#!/usr/bin/python3

from gpiozero import LEDBarGraph
from time import sleep

graph = LEDBarGraph(4, 17, 22, 5, 13, 26)

graph.value = 1
sleep(1)
graph.value = 1/2
sleep(1)
graph.value = -1/2
sleep(1)
graph.value = 1/4
sleep(1)
graph.value = -1
sleep(1)
