from Adafruit_PWM_Servo_Driver import PWM
import RPi.GPIO as GPIO
import time
import sys
import serial

ser = serial.Serial("/dev/ttyAMA0", 9600)
pwm = PWM(0x40, debug = False)
channel = 1
GPIO.setmode(GPIO.BCM)
pwm.setPWMFreq(50)
"""

pulse_width = int(0.4*4096/20) just approxiate

"""
# [232,380] clamp range
# [90, 275 ,500] base range
# [160,465] main arm
# [210,375] side arm



class Component:
    """
    Arg:
        name: str; name of component
        channel: int; location of pin
        pw_min: the minimum pulse of the component, default = 90
        pw_max: the maximum pulse of the component, default = 500
        pw_init: the initial pulse of the component, default = 275
        
        eg.

        # [232,380] clamp range
        # [90, 275 ,500] base range
        # [160,465] main arm
        # [210,375] side arm
    """
    def __init__(self, name,  channel, pw_min = 90, pw_max = 500, pw_init = 275):
        self.name = name
        self.channel = channel
        self.pw_min = pw_min
        self.pw_max = pw_max
        self.pw_init = pw_init
        self.pw_current = pw_init
        self.move_arm(pw_init)
    
    def move_arm(self, pulse_width):
        pwm.setPWM(self.channel,0,pulse_width)
        self.pw_current = pulse_width
        time.sleep(0.01)

    def test(self):
        print(f"Testing {self.name}...")
        for i in range(self.pw_current, self.pw_max+1):
            self.move_arm(i)
        for i in range(self.pw_current, self.pw_min, -1):
            self.move_arm(i)
        for i in range(self.pw_current, self.pw_init,1):
            self.move_arm(i)
        print(f"{self.name}'s test completed.")

component_1 = Component("clamp", channel = 0, pw_min = 232, pw_max = 380, pw_init = 232)
component_2 = Component("main_arm", channel = 1, pw_min = 160, pw_max = 465, pw_init = 300)
component_3 = Component("side_arm", channel = 2, pw_min = 210, pw_max = 375, pw_init = 210)
component_4 = Component("base", channel = 3, pw_min = 90, pw_max = 500, pw_init = 275)
components_list = [component_1, component_2, component_3, component_4]


if __name__ == "__main__":
    for component in components_list:
        component.test()