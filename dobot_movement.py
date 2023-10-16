import RPi.GPIO as GPIO
import time
from pydobot import Dobot

device = Dobot(port="/dev/ttyUSB0", verbose=False)

button_pin = 16
servo1_pin = 4
servo2_pin = 7

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(servo1_pin, GPIO.OUT)
GPIO.setup(servo2_pin, GPIO.OUT)


def code1():
    print("Code 1 실행")
    device.move_to(165,234,70,73,wait=False)
    print('1')
   
    device.move_to(155,207,11,73,wait=False)
    print('2')

    device.move_to(174,227,64,73,wait=False)
    print('3')

    device.move_to(155,207,11,73,wait=False)
    print('4')

    device.move_to(174,227,64,73,wait=False)
    print('5')

    device.move_to(174,225,76,72,wait=False)
    print('6')

    device.move_to(-93,250,68,-89,wait=False)
    print('7')

    device.move_to(-78,250,71,-84,wait=False)
    print('8')

    device.move_to(-82,250,82,-84,wait=False)
    print('9')

    device.move_to(-86,296,87,-86,wait=False)
    print('10')

    device.move_to(-89,293,99,-86,wait=False)
    print('11')

    device.move_to(-89,295,73,-86,wait=False)
    print('12')

    device.move_to(-90,296,80,-87,wait=False)
    print('13')

    device.move_to(274,-32,8,13,wait=False)
    print('14')

    device.move_to(174,252,49,75,wait=False)
    print('15')

    device.move_to(164,232,1,74,wait=False)
    print('16')

    device.move_to(179,252,64,74,wait=False)
    print('17')

    device.move_to(164,231,1,74,wait=False)
    print('18')

    device.move_to(161,228,-6,74,wait=False)
    print('19')

    device.move_to(177,250,49,74,wait=False)
    print('20')

    device.move_to(198,-3,13,18,wait=False)
    print('21')


def code2():
    print("Code 2 실행")

    pwm1 = GPIO.PWM(servo1_pin, 50)
    pwm2 = GPIO.PWM(servo2_pin, 50)

    pwm1.start(0)
    pwm2.start(0)

    try:
        while True:
           
            for angle in range(0, 181, 10):
                duty_cycle_11 = angle /18 +2.5
                duty_cycle_22 =(180-angle)/18+25
               
                pwm1.ChangeDutyCycle(duty_cycle_11 )
                pwm2.ChangeDutyCycle(duty_cycle_22 )
               
                time.sleep(0.3) 
           
            for angle in range(180, -1, -10):
                duty_cycle_11 = angle /18 +2.5 
                duty_cycle_22 =(180-angle)/18+25
               
                pwm1.ChangeDutyCycle(duty_cycle_11 )
                pwm2.ChangeDutyCycle(duty_cycle_22 )
               
                time.sleep(0.3) 
   
    except KeyboardInterrupt:
        pass
   
    finally:
        pwm1.stop()
        pwm2.stop()


while True:
    if GPIO.input(button_pin) == GPIO.HIGH:
        print("Button pushed!")
        code1()
        code2()
        time.sleep(0.5)  

    time.sleep(0.1)