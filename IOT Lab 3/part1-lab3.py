# CIT 381 - Spring 2024
# Author: Angel Munoz
# Created: Feburary 6,2024
# Sets up distance sensor and prints the distance

from gpiozero import DistanceSensor
import time

sensor = DistanceSensor(echo=27, trigger=17)

while True:
        print('Distance: ', sensor.distance * 100)
        time.sleep(1)