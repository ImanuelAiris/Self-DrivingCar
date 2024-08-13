import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

buzzer = 25

trigger = 5
echo = 6

red = 17
yellow = 27
green = 22

GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

global buzz
buzz = GPIO.PWM(buzzer, 440)

def safety():
    GPIO.output(trigger, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
    if distance <= 15:
        buzz.start(50)
        GPIO.output(red, GPIO.HIGH)
        GPIO.output(yellow, GPIO.LOW)
        GPIO.output(green, GPIO.LOW)
    else:
        buzz.stop()
        GPIO.output(red, GPIO.LOW)
        GPIO.output(yellow, GPIO.LOW)
        GPIO.output(green, GPIO.HIGH)
    return distance