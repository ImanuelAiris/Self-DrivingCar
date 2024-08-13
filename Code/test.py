import serial
import RPi.GPIO as GPIO

LED = 21
state = 0
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
ser.reset_input_buffer()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED,GPIO.OUT)

def temp():
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        temp = float(line.split(' ')[4].replace('C',''))
        hum = float(line.split(' ')[1].replace('%', ''))
        print(hum)       
        if temp > 25:
            GPIO.output(LED,GPIO.HIGH)
            state = 1
        else:
            GPIO.output(LED,GPIO.LOW)
            state = 0
        return temp
    else:
        return 0
   
if __name__ == '__main__':
    while True:
        temp()
