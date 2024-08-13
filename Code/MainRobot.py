con = False 
from MotorModule import Motor
from LaneDetectionModule import getLaneCurve
from ArduinoModule import temp
from time import sleep
import WebcamModule
from Safety import safety
import cv2

##################################################
motor = Motor(18, 15, 14, 13, 24, 23)
##################################################

def main():
    img = WebcamModule.getImg()
    curveVal= getLaneCurve(img,1)
    motorspeed = 0.4
    sen = 2.4   # SENSITIVITY
    maxVAl= 0.55 # MAX SPEED
    if curveVal>maxVAl: curveVal = maxVAl
    if curveVal<-maxVAl: curveVal =-maxVAl
    #print(curveVal)
    if curveVal>0:
        if curveVal<0.05:curveVal=0
    else:
        if curveVal>-0.08:curveVal=0

    distance = safety()
    if distance <= 15:
        while True:
            motor.stop()

    else:
        while True:
            motor.move(motorspeed,-curveVal*sen,0.0001)
 
if __name__ == '__main__':
    while True:
        main()


