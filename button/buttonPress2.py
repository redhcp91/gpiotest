
from gpiozero import LED, LEDBoard, PWMLED, Button
from signal import pause

leds = LEDBoard(4, 17, 22, 10, pwm=True)
button1 = Button(6, hold_time=.2)
button2 = Button(19, hold_time=.2)

button1.when_pressed = leds.on
button2.when_pressed = leds.off


button2.when_held = leds.pulse
button1.when_held = leds.blink

pause()



