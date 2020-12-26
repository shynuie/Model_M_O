import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

record = []

for i in range(30):
    j = i+1
    GPIO.setup(j, GPIO.OUT)
    print(f'Testing chanel : {j} ')
    GPIO.output(j, True)
    time.sleep(2)
    component = input('Enter the component name:')
    record.append([j, component])
    GPIO.cleanup()

print(record)