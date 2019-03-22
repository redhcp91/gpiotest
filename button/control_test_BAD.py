
import os
from time import sleep
from gpiozero import Button, PWMLED

led_choice = 0
count = 0

os.system('clear')

print("Which LED do you want to blink")
print("1: Blue?")
print("2: Green?")
print("3: Yellow?")
print("4: Red?")
print("5: All")
led_choice = input("Make your choice: ")

if led_choice == 1:
    os.system('clear')
    print("You choose the Blue LED.")
    count = input("Number of times to blink?")
    while count > 0:

    print("")
    print("")
    print("")

