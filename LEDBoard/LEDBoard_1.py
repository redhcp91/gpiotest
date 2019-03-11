#!/usr/bin/python3

from gpiozero import LEDBoard
from time import sleep
from signal import pause

leds = LEDBoard(4, 17, 22)

leds.on()
sleep(1)
leds.off()
sleep(1)
leds.value = (1, 0, 1)
sleep(1)
leds.blink()

pause()
