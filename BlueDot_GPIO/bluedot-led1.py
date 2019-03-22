
import os
from bluedot import BlueDot
from gpiozero import LED, Button
from time import sleep
from signal import pause

bd = BlueDot()

led1 = LED(4)
led2 = LED(17)
led3 = LED(27)
led4 = LED(22)
button1 = Button(10)

while True:
    bd.wait_for_press()
    led1.toggle()
    led2.toggle()
    led3.toggle()
    led4.toggle()
    sleep(0.5)

pause()
