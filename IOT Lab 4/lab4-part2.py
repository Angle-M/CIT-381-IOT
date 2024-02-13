from gpiozero import MotionSensor, Button, LED
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define GPIO pin numbers
motion = MotionSensor(21)
push_button = Button(17)
reed_switch = Button(18, pull_up=False)
armed_led = LED(23)  # Changed GPIO pin
alarm_led = LED(22)

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
    if armed and (motion.when_motion or reed_switch.is_activated):
        print("ALARM ACTIVATED!")
        alarm_led.on()
        send_email("ALERT: Alarm Activated", "Motion detected or reed switch opened.")
        alarm_triggered = True
    else:
        alarm_triggered = False

def clear_alarm():
    if (motion.when_no_motion or reed_switch.is_deactivated):
        print("Alarm Cleared")
        clear_alarm = True
        alarm_led.off()

motion.when_motion = handle_alarm
motion.when_no_motion = clear_alarm
reed_switch.when_activated = handle_alarm
reed_switch.when_deactivated = clear_alarm
push_button.when_pressed = arm_system

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    print("Exiting the program.")
    armed_led.off()
    alarm_led.off()
