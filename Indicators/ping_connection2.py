#!/usr/bin/python3

from gpiozero import LED, PingServer
from gpiozero.tools import negated
from signal import pause

green = LED(17)
red = LED(22)

RPIold = PingServer('192.168.2.106')

green.source = RPIold
green.source_delay = 5
red.source = negated(green)

pause()
