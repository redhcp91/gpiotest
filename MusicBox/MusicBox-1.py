#!/usr/bin/python3

from gpiozero import Button
import pygame.mixer
from pygame.mixer import Sound
from signal import pause

pygame.mixer.init()

button_sounds = {
        Button(6): Sound("samples/drum_tom_hard.wav"),
        Button(19): Sound(""),
}

for button, sound  in button_sounds.items():
    button.when_pressed = sound.play

pause()
