import RPi.GPIO as GPIO
import time

class Direction:
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        R_EN = 21
        L_EN = 22
        RPWM = 23
        LPWM = 24

        SERVO = 17

        GPIO.setup(R_EN, GPIO.OUT)
        GPIO.setup(RPWM, GPIO.OUT)
        GPIO.setup(L_EN, GPIO.OUT)
        GPIO.setup(LPWM, GPIO.OUT)
        GPIO.setup(SERVO, GPIO.OUT)

        GPIO.output(R_EN, GPIO.HIGH)
        GPIO.output(L_EN, GPIO.HIGH)

        self.my_pwm = GPIO.PWM(RPWM,100)
        self.my_pwm1 = GPIO.PWM(LPWM,100)
        self.servo = GPIO.PWM(SERVO, 50)

        self.my_pwm.start(50)
        self.my_pwm1.start(50)
        self.servo.start(0)

    def neutral(self):
        self.my_pwm.ChangeDutyCycle(0)
        self.my_pwm1.ChangeDutyCycle(0)

    def foward(self):
        self.servo.ChangeDutyCycle(self.angle_to_percent(90))
        self.my_pwm.ChangeDutyCycle(14)
        self.my_pwm1.ChangeDutyCycle(0)

    def backward(self):
        self.my_pwm.ChangeDutyCycle(0)
        self.my_pwm1.ChangeDutyCycle(30)
    
    def left(self):
        self.servo.ChangeDutyCycle(6.15)
        time.sleep(0.010)
        self.servo.ChangeDutyCycle(0)

    def right(self):
        self.servo.ChangeDutyCycle(8.15)
        time.sleep(0.010)
        self.servo.ChangeDutyCycle(0)
    
    def angle_to_percent(self, angle) :
        if angle > 180 or angle < 0 :
            return False

        start = 4
        end = 12.5
        ratio = (end - start)/180 #Calcul ratio from angle to percent

        angle_as_percent = angle * ratio

        return start + angle_as_percent
