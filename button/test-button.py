#!/usr/bin/python3

from gpiozero import LED, Button
from time import sleep
from signal import pause

led1 = LED(4)
led2 = LED(17)

button1 = Button(26)

while True:
    button1.wait_for_press()
    led1.toggle()
    led2.toggle()
    sleep(0.5)


