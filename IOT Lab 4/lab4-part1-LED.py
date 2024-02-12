from gpiozero import LED
import time

# Define the LED objects for the Armed and Alarm LEDs
armed_led = LED(21)
alarm_led = LED(22)

def test_armed_and_alarm_leds():
    # Turn on the Armed LED
    armed_led.on()
    print("Armed LED is ON")

    # Wait for 2 seconds
    time.sleep(2)

    # Turn off the Armed LED and turn on the Alarm LED
    armed_led.off()
    alarm_led.on()
    print("Armed LED is OFF, Alarm LED is ON")

    # Wait for 2 seconds
    time.sleep(2)

    # Turn off the Alarm LED
    alarm_led.off()
    print("Alarm LED is OFF")

try:
    while True:
        test_armed_and_alarm_leds()
        time.sleep(1)

except KeyboardInterrupt:
    # Clean up GPIO on program exit
    armed_led.off()
    alarm_led.off()
    print("Program terminated by user. GPIO cleanup complete.")
