
from bluedot import BlueDot
from gpiozero import PWMLED
from signal import pause


def set_brightness(pos):
    brightness = (pos.y + 1) / 2
    led.value = brightness


led = PWMLED(22)
bd = BlueDot()
bd.when_moved = set_brightness

pause()
