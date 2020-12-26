import RPi.GPIO as GPIO
import time

class Moving:

    """
    Moving class

    Method:
        act(action, speed, duration)

    """
    def __init__(self):
        self._PWMA = 18
        self._AIN1 = 22  # Ahead
        self._AIN2 = 27  # Back
        self._PWMB = 23
        self._BIN1 = 24   # Ahead
        self._BIN2 = 25   # Back
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._AIN2, GPIO.OUT)
        GPIO.setup(self._AIN1, GPIO.OUT)
        GPIO.setup(self._PWMA, GPIO.OUT)
        GPIO.setup(self._BIN2, GPIO.OUT)
        GPIO.setup(self._BIN1, GPIO.OUT)
        GPIO.setup(self._PWMB, GPIO.OUT)
        self._L_Motor = GPIO.PWM(self._PWMA, 100)
        self._L_Motor.start(0)
        self._R_Motor = GPIO.PWM(self._PWMB, 100)
        self._R_Motor.start(0)
    

    def act(self, action = 0, speed=0, duration = 0):
        '''
        Arg:
            action: int '0' for stop, 'w' for foward, 'a' for turn left, 'd' for turn right, 's' for backward
            speed: int
            duration: int, the duration time for the action
        '''
        if action == 0:
            self._stop(duration)
        elif action == 'w':
            self._ahead(speed = speed, duration = duration)
        elif action == 'a':
            self._left(speed = speed, duration = duration)
        elif action == 'd':
            self._right(speed = speed, duration = duration)
        elif action == 's':
            self._back(speed = speed, duration = duration)


    def _ahead(self, speed = 0, duration = 0):
        self._L_Motor.ChangeDutyCycle(speed)
        GPIO.output(self._AIN2, False) 
        GPIO.output(self._AIN1, True)

        self._R_Motor.ChangeDutyCycle(speed)
        GPIO.output(self._BIN2, False)
        GPIO.output(self._BIN1, True)
        time.sleep(duration)

    def _stop(self, duration = 0):
        self._L_Motor.ChangeDutyCycle(0)
        GPIO.output(self._AIN2, False) 
        GPIO.output(self._AIN1, False)

        self._R_Motor.ChangeDutyCycle(0)
        GPIO.output(self._BIN2, False)
        GPIO.output(self._BIN1, False)
        time.sleep(duration)    


    def _back(self, speed = 0, duration = 0):
        self._L_Motor.ChangeDutyCycle(speed)
        GPIO.output(self._AIN2, True) 
        GPIO.output(self._AIN1, False)

        self._R_Motor.ChangeDutyCycle(speed)
        GPIO.output(self._BIN2, True)
        GPIO.output(self._BIN1, False)
        time.sleep(duration)  


    def _left(self, speed=0, duration = 0):
        self._L_Motor.ChangeDutyCycle(speed)
        GPIO.output(self._AIN2, True) 
        GPIO.output(self._AIN1, False)

        self._R_Motor.ChangeDutyCycle(speed)
        GPIO.output(self._BIN2, False)
        GPIO.output(self._BIN1, True)
        time.sleep(duration)  


    def _right(self, speed = 0, duration = 0):
        self._L_Motor.ChangeDutyCycle(speed)
        GPIO.output(self._AIN2, False) 
        GPIO.output(self._AIN1, True)

        self._R_Motor.ChangeDutyCycle(speed)
        GPIO.output(self._BIN2, True)
        GPIO.output(self._BIN1, False)
        time.sleep(duration)  

if __name__ == "__main__":
    action = Moving()
    try:
        while True:
            action.act(action='w',speed=30, duration=1)
            action.act(action='a',speed=30, duration=1)
            action.act(action='d',speed=30, duration=1)
            action.act(action='s',speed=30, duration=1)
            action.act(action= 0 ,speed=30, duration=1)    
    except KeyboardInterrupt:
        GPIO.cleanup()
    pass