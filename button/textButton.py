#!/usr/bin/python3.5

from gpiozero import Button
from signal import pause

def say_pressed():
    print("Button Pressed")


def say_unpressed():
    print("Button Let Go")


button = Button(10)

button.when_pressed = say_pressed
button.when_released = say_unpressed

pause()
