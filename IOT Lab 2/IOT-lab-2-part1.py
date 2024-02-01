#CIT 381 - Spring 2024
# Author: Angel Munoz
# Created: January 29,2024
# simple loop to make led blink

import time
from gpiozero import LED

led = LED(17, active_high = False)
while True:
        led.on()
        time.sleep(1)
        led.off()
        time.sleep(1)