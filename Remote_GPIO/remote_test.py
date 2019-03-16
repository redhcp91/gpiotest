from gpiozero import LED
from time import sleep

blue = LED(4)

while True:
    blue.on()
    sleep(1)
    blue.off()
    sleep(1)
