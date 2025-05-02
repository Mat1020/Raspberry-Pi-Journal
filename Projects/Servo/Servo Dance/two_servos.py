from gpiozero import AngularServo
from time import sleep

servo_1 = AngularServo(18, min_pulse_width=0.0006,
                     max_pulse_width=0.0023)

servo_2 = AngularServo(14, min_pulse_width=0.0006,
                     max_pulse_width=0.0023)

while (True):
    servo_1.angle = 90
    servo_2.angle = 90
    sleep(2)
    servo_1.angle = 0
    servo_2.angle = 0
    sleep(2)
    servo_1.angle = -90
    servo_2.angle = -90
    sleep(2)
