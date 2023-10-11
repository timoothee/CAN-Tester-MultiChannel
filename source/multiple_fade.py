import RPi.GPIO as GPIO
import time
import multiprocessing as mp
import threading
class rgb_fade():
    def __init__(self):
        self.led1_modify = 2500
        self.add = 0.01
        self.led1_add_1 = 0.001
        self.led1_add_2 = 0.01
        self.led2_add_1 = 0.001
        self.led2_add_2 = 0.01
        self.led3_add_1 = 0.001
        self.led3_add_2 = 0.01
        self.led4_add_1 = 0.001
        self.led4_add_2 = 0.01
        self.led1_delay = 1/self.led1_modify

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    def setup(self, gpio):
        GPIO.setup(gpio,GPIO.OUT)
        GPIO.output(gpio,GPIO.LOW)

    def fade_out(self, gpio, add1, add2):
        for i in range(int(self.led1_modify/100)):
            GPIO.output(gpio,GPIO.LOW)
            time.sleep(add2 - self.led1_delay)
            GPIO.output(gpio,GPIO.HIGH)
            time.sleep(add1 + self.led1_delay)
 
            add2 = add2 - self.led1_delay
            add1 = add1 + self.led1_delay

            print(i, add2, add1)


    def fade_in(self, gpio, add1, add2):
        for i in range(int(self.led1_modify/100)):
            GPIO.output(gpio,GPIO.LOW)
            time.sleep(add1 + self.led1_delay)
            GPIO.output(gpio,GPIO.HIGH)
            time.sleep(add2 - self.led1_delay)

            add2 = add2 - self.led1_delay
            add1 = add1 + self.led1_delay

            print(i, add2, add1)

    def initial_state(self, add1, add2):
        self.add1 = 0.001
        self.add2 = 0.01


faiding = rgb_fade()

faiding.setup(4)
faiding.setup(18)
faiding.setup(15)
faiding.setup(17)

def lop():
    looop(4, faiding.led1_add_1, faiding.led1_add_2)

def lop1():
    looop(15, faiding.led2_add_1, faiding.led2_add_2)
def lop2():
    looop(18, faiding.led3_add_1, faiding.led3_add_2)

def lop3():
    looop(17, faiding.led4_add_1, faiding.led4_add_2)

def looop(gpio, add1, add2):
    for i in range(10):
        faiding.fade_out(gpio, add1, add2)
        faiding.initial_state(add1, add2)
        faiding.fade_in(gpio, add1, add2)
        faiding.initial_state(add1, add2)

threading.Thread(target=lop).start()
threading.Thread(target=lop1).start()
threading.Thread(target=lop2).start()


