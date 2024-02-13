from gpiozero import MotionSensor
from gpiozero import Button
import time

motion = MotionSensor(21)

# Loop to test the motion sensor

while True:
    motion.wait_for_motion()
    print("Motion Detected!")
    time.sleep(1)
    

