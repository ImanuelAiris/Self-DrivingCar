from MotorModule import Motor
from TestController import getJS
from time import sleep

##################################################
motor = Motor(18, 15, 14, 13, 24, 23)
##################################################

def controller():
    JS = getJS()
    X = JS['axis1']
    Y = JS['axis2']
    if Y < 0:
        S = ((-Y)*0.5) + 0.5
    elif Y > 0:
        S = -(Y*0.5) - 0.5
    else:
        motor.stop()
        S = 0
    print('S:{}'.format(S))
    motor.move(S, (-X))
    sleep(0.1)
    
if __name__ == '__main__':
    while True:
        controllerMotor()