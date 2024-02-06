#CIT 381 - Spring 2024
# Author: Angel Munoz
# Created: Feburary 6,2024
# Sets up distance sensor and lights up LEDs based on distance and turns them off based on distance

from gpiozero import DistanceSensor
from gpiozero import LED
import time

led1 = LED(24, active_high = False)
led2 = LED(21, active_high = False)
led3 = LED(26, active_high = False)

led1.off()
led2.off()
led3.off()

sensor = DistanceSensor(echo=6, trigger=5, max_distance=5)

while True:
        distance = int(sensor.distance * 100)
        if distance > 0 and distance < 100:
                led1.on()
                led2.off()
                led3.off()
        elif distance >= 100 and distance < 200:
                led1.on()
                led2.on()
                led3.off()
        else:
                led1.on()
                led2.on()
                led3.on()
        print('Distance: ', distance)
        time.sleep(5)

