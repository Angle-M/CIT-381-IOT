from gpiozero import Button
import time

push_button = Button(17)
reed_switch = Button(18, pull_up=False)

def push_button_callback():
    print("Push Button Pressed")

def reed_switch_callback():
    if reed_switch.is_active:
        print("Reed Switch: Closed (Magnet Attached)")
    else:
        print("Reed Switch: Open (Magnet Removed)")

# Assign callback functions to events
push_button.when_pressed = push_button_callback
reed_switch.when_actived = reed_switch_callback
reed_switch.when_deactivated = reed_switch_callback


while True:
    time.sleep(1)
    