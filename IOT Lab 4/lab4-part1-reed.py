from gpiozero import Button
import time

# Define the Button objects for the push button and reed switch
push_button = Button(17)
reed_switch = Button(18)

def push_button_callback():
    print("Push Button Pressed")

def reed_switch_callback():
    if reed_switch.is_pressed:
        print("Reed Switch: Closed (Magnet Attached)")
    else:
        print("Reed Switch: Open (Magnet Removed)")

# Assign callback functions to events
push_button.when_pressed = push_button_callback
reed_switch.when_pressed = reed_switch_callback


while True:
    time.sleep(1)
    