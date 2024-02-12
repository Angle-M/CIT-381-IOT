# Testing the HC-SR501 motion sensor
# The motion sensor needs to be connected to GPIO 21
# If the time delay is set to the minimum we should see the message print 3-4 times
# Import object from GPIOZERO and time library

from gpiozero import MotionSensor
from gpiozero import Button
import time

# Define the motion sensor
motion = MotionSensor(21)

# Loop to test the motion sensor

while True:
    motion.wait_for_motion()
    print("Motion Detected!")
    # Sleep for 1 seconds so we don't get a whole bunch of messages
    # We should get 3-4 messages on each activation.
    time.sleep(1)
    

