#CIT 381 - Spring 2024
# Author: Angel Munoz
# Created: January 29,2024
# simple loop to make led blink when pushing a button

#importing libraries
import time
from gpiozero import LED
from gpiozero import Button

led = LED(17, active_high=False)
button = Button(27, bounce_time=0.26)

number = 0

while True:
    if button.value == 1:
        number += 1
        print("Button was pressed " + str(number) + " times")
        for i in range(number):
            led.blink(on_time=1, off_time=1, n=5)
            time.sleep(5)
