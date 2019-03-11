#!/usr/bin/python3

from gpiozero import LED, PingServer
from gpiozero.tools import negated
from signal import pause

green = LED(17)
red = LED(4)

google = PingServer('8.8.8.8')

green.source = google
green.source_delay = 60
red.source = negated(green)

pause()
