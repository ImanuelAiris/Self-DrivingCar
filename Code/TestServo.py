import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

In1, In2, In3, In4, Ena, Enb = 14, 15, 23, 24, 18, 13
GPIO.setup(In1, GPIO.OUT)
GPIO.setup(In2, GPIO.OUT)
GPIO.setup(In3, GPIO.OUT)
GPIO.setup(In4, GPIO.OUT)
GPIO.setup(Ena, GPIO.OUT)
GPIO.setup(Enb, GPIO.OUT)
pwma = GPIO.PWM(Ena, 100)
pwmb = GPIO.PWM(Enb, 100)
pwma.start(0)
pwmb.start(0)

while True:
    print('Backward')
    GPIO.output(In1, GPIO.HIGH)
    GPIO.output(In2, GPIO.LOW)
    GPIO.output(In3, GPIO.HIGH)
    GPIO.output(In4, GPIO.LOW)
    pwma.ChangeDutyCycle(100)
    pwmb.ChangeDutyCycle(100)
    
    sleep(2)
    print('Forward')
    GPIO.output(In1, GPIO.LOW)
    GPIO.output(In2, GPIO.HIGH)
    GPIO.output(In3, GPIO.LOW)
    GPIO.output(In4, GPIO.HIGH)
    sleep(2)
    