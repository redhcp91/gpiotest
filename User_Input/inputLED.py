
from gpiozero import LED, Button
from signal import pause

print('Input button number')
button = input()

print('Input LED1 number')
led1 = input()

print('Input LED2 number')
led2 = input()

button.when_pressed = led1.toggle()
button.when_held = led2.toggle()

pause()
