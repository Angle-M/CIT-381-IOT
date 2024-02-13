from gpiozero import MotionSensor, Button, LED
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define GPIO pin numbers
motion_sensor_pin = 17
reed_switch_pin = 18
arm_button_pin = 19
armed_led_pin = 21
alarm_led_pin = 22

# Initialize global variables
armed = False
alarm_triggered = False

# Initialize components
motion_sensor = MotionSensor(motion_sensor_pin)
reed_switch = Button(reed_switch_pin)
arm_button = Button(arm_button_pin)
armed_led = LED(armed_led_pin)
alarm_led = LED(alarm_led_pin)

# Email configuration
email_address = "your_email@gmail.com"
email_password = "your_email_password"
recipient_email = "recipient_email@example.com"

def send_email(subject, body):
    try:
        # Set up the MIME
        message = MIMEMultipart()
        message['From'] = email_address
        message['To'] = recipient_email
        message['Subject'] = subject

        # Attach the body to the email
        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server, send the email, and close the connection
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(email_address, email_password)
            server.sendmail(email_address, recipient_email, message.as_string())
    except Exception as e:
        print(f"Error sending email: {e}")

def arm_system():
    global armed
    armed = not armed

    if armed:
        print("System Armed")
        armed_led.on()
    else:
        print("System Disarmed")
        armed_led.off()
        

def handle_alarm():
    global alarm_triggered
    if armed and (motion_sensor.motion_detected or reed_switch.is_pressed):
        if not alarm_triggered:
            print("ALARM ACTIVATED!")
            alarm_led.on()
            send_email("ALERT: Alarm Activated", "Motion detected or reed switch opened.")
            alarm_triggered = True
    else:
        alarm_triggered = False

def clear_alarm():
    if not (motion_sensor.motion_detected or reed_switch.is_pressed):
        print("Alarm Cleared")
        alarm_led.off()

# Assign callback functions to events
motion_sensor.when_motion = motion_detected
reed_switch.when_pressed = reed_switch_state_change
arm_button.when_pressed = arm_system

try:
    while True:
        handle_alarm()
        clear_alarm()
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting the program.")
    armed_led.off()
    alarm_led.off()
