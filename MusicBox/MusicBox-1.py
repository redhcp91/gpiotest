#!/usr/bin/python3

from gpiozero import Button
import pygame.mixer
from pygame.mixer import Sound
from signal import pause

pygame.mixer.init()

button_sounds = {
        Button(26): Sound("/home/pi/samples/1000Hz.wav"),
}

for button, sound in button_sounds.items():
    button.when_pressed = sound.play

pause()
