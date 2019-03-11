from gpiozero import LEDBoard, Button
from time import sleep
from signal import pause

leds = LEDBoard(4, 17, 22, 10)
button = Button(6)

button.when_pressed = leds.on

pause()
