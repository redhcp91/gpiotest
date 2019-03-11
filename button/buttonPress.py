
from gpiozero import LED, LEDBoard, Button
from signal import pause

leds = LEDBoard(4, 17, 22, 10)
button1 = Button(6)
button2 = Button(19)

button1.when_pressed = leds.on
button2.when_pressed = leds.off

pause()



