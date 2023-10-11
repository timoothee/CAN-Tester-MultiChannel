import RPi.GPIO as GPIO
import time
import threading


class rgb_fade():
    def __init__(self):
        self.modify = 2500
        self.add = 0.001
        self.add_1 = 0.001 # default 0.001
        self.add_2 = 0.01   # default 0.01
        self.delay = 1/self.modify
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        global repe_t
        repe_t = 4

    def fade_out(self, gpio):
        GPIO.setup(gpio,GPIO.OUT)
        for i in range(int(self.modify/100)):

            GPIO.output(gpio,GPIO.LOW)
            time.sleep(self.add_2 - self.delay)
            GPIO.output(gpio,GPIO.HIGH)
            time.sleep(self.add_1 + self.delay)
 
            self.add_2 = self.add_2 - self.delay
            self.add_1 = self.add_1 + self.delay

            #print(i, self.add_2, self.add_1)


    def fade_in(self, gpio):
        GPIO.setup(gpio,GPIO.OUT)
        for i in range(int(self.modify/100)):

            GPIO.output(gpio,GPIO.LOW)
            time.sleep(self.add_1 + self.delay)
            GPIO.output(gpio,GPIO.HIGH)
            time.sleep(self.add_2 - self.delay)

            self.add_2 = self.add_2 - self.delay
            self.add_1 = self.add_1 + self.delay

            #print(i, self.add_2, self.add_1)

    def initial_state(self, gpio):
        self.add_1 = 0.001
        self.add_2 = 0.01

def new_func1():
    faiding = rgb_fade()
    for i in range(repe_t):
        faiding.fade_out(4)
        faiding.initial_state(4)
        #time.sleep(1)
        faiding.fade_in(4)
        faiding.initial_state(4)
def new_func2():
    faiding = rgb_fade()
    for i in range(repe_t):
        faiding.fade_out(17)
        faiding.initial_state(17)
        #time.sleep(1)
        faiding.fade_in(17)
        faiding.initial_state(17)
def new_func3():
    faiding = rgb_fade()
    for i in range(repe_t):
        faiding.fade_out(27)
        faiding.initial_state(27)
        #time.sleep(1)
        faiding.fade_in(27)
        faiding.initial_state(27)
def new_func4():
    faiding = rgb_fade()
    for i in range(repe_t):
        faiding.fade_out(22)
        faiding.initial_state(22)
        #time.sleep(1)
        faiding.fade_in(22)
        faiding.initial_state(22)
def new_func5():
    faiding = rgb_fade()
    for i in range(repe_t):
        faiding.fade_out(5)
        faiding.initial_state(5)
        #time.sleep(1)
        faiding.fade_in(5)
        faiding.initial_state(5)
def new_func6():
    faiding = rgb_fade()
    for i in range(repe_t):
        faiding.fade_out(6)
        faiding.initial_state(6)
        #time.sleep(1)
        faiding.fade_in(6)
        faiding.initial_state(6)
def new_func7():
    faiding = rgb_fade()
    for i in range(repe_t):
        faiding.fade_out(13)
        faiding.initial_state(13)
        #time.sleep(1)
        faiding.fade_in(13)
        faiding.initial_state(13)
def new_func8():
    faiding = rgb_fade()
    for i in range(repe_t):
        faiding.fade_out(26)
        faiding.initial_state(26)
        #time.sleep(1)
        faiding.fade_in(26)
        faiding.initial_state(26)

t1 = threading.Thread(target=new_func1)
t2 = threading.Thread(target=new_func2)
t3 = threading.Thread(target=new_func3)
t4 = threading.Thread(target=new_func4)
t5 = threading.Thread(target=new_func5)
t6 = threading.Thread(target=new_func6)
t7 = threading.Thread(target=new_func7)
t8 = threading.Thread(target=new_func8)

def leds_init():
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
