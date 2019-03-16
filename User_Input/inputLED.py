
from gpiozero import LED, Button
from signal import pause

print('Input button number')
button = input()

print('Input LED1 number')
led1 = input()

print('Input LED2 number')
led2 = input()

<<<<<<< HEAD
button.when_pressed = led1.toggle()
button.when_held = led2.toggle()
=======
button.when_pressed = led1.toggle
button.when_held = led2.toggle
>>>>>>> 29000bb19113ec34e07b13adf72c0ee93cc9e33a

pause()
