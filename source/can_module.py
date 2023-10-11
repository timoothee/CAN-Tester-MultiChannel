import os
import time
import RPi.GPIO as GPIO

class CanModule():
    def __init__(self, txquelen = 1000, baudrate = 1000000, dbaudrate = 5000000, sample_point = 0.750, dsample_point = 0.750):
        self.txquelen = txquelen
        self.baudrate = ""
        self.dbaudrate = ""
        self.frame_que = []
        self.module_name = ""
        self.sample_point = sample_point
        self.dsample_point = ''
        self.can_status_var = False
        self.mux_led_pos = [4, 17, 27, 22, 5, 6, 13, 26]
        self.sel_pins = [23, 16, 7]
        self.msg = ''
        self.flag_msg = 0
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(14, GPIO.OUT)
        GPIO.output(14,GPIO.LOW) 
        self.rasp_path = str((os.popen("pwd", 'r', 128)).read()).strip().replace('/source', '/logs/')
        for item in self.mux_led_pos:
            GPIO.setup(item, GPIO.OUT)

    def set_mux_sel(self, selection: str):
        for i in range(2, -1, -1):
            GPIO.setup(self.sel_pins[i], GPIO.OUT)
            GPIO.output(self.sel_pins[i], int(selection[0]))
            selection = selection[1:]

    def set_messages(self, mesg: int):
        self.msg = mesg

    def get_messages(self):
        return self.msg

    def set_message_flag(self, msg: int):
        self.flag_msg = msg

    def get_message_flag(self):
        return self.flag_msg

    def set_rasp_path(self, path):
        self.rasp_path = path

    def get_rasp_path(self):
        return self.rasp_path

    def set_can_status(self, status):
        self.can_status_var = status

    def get_can_status(self):
        return self.can_status_var

    #module name
    def set_module_name(self, name):
        self.module_name = name
    
    def get_can_module_name(self):
        return self.module_name
    
    #baudrate
    def set_baudrate(self, baudrate):
        self.baudrate = baudrate

    def get_baudrate(self):
        return self.baudrate
    
    #dbaudrate
    def set_dbaudrate(self, dbaudrate):
        self.dbaudrate = dbaudrate

    def get_dbaudrate(self):
        return self.dbaudrate
    
    #sample point
    def set_sample_point(self, sample_point):
        self.sample_point = sample_point
    
    def get_sample_point(self):
        response = os.popen(f"ip -d -s link show {self.module_name}", 'r', 128)
        response = response.read()
        for line in response.split('\n'):
            if 'sample-point' in line:
                return line.split()[-1]

    #dsample-point
    def set_dsample_point(self, dsample_point):
        if dsample_point == '':
            dsample_point = '0.750'
        self.dsample_point = dsample_point

    def get_dsample_point(self):
        response = os.popen(f"ip -d -s link show {self.module_name}", 'r', 128)
        response = response.read()
        for line in response.split('\n'):
            if 'dsample-point' in line:
                return line.split()[-1]

    
    def interface_up(self):
        os.popen(f"sudo ip link set {self.module_name} up type can bitrate {self.baudrate}  dbitrate {self.dbaudrate} restart-ms 1000 berr-reporting on fd on dsample-point {self.dsample_point}", 'w', 128)
        print(f"sudo ip link set {self.module_name} up type can bitrate {self.baudrate}  dbitrate {self.dbaudrate} restart-ms 1000 berr-reporting on fd on dsample-point {self.dsample_point}")
        os.popen(f"sudo ifconfig {self.module_name} txqueuelen 65536", 'w', 128)
        print(f"sudo ifconfig {self.module_name} txqueuelen 65536")        
    
    def can_dump(self):
        print("start")
        os.popen(f"cat {self.rasp_path}can.log")
        os.popen(f"candump {self.module_name} > {self.rasp_path}can.log", "w", 128)
        print("end")

    def interface_down(self):
        os.popen(f"sudo ip link set {self.module_name} down",'w', 128)

    def send_q(self, id_list: str, brs_list, payload_list, fd_list, led_pin: int):
        self.set_messages(1)
        print(f"module name {self.module_name}, id list {id_list}, brs {brs_list}, payload {payload_list}")
        if payload_list == "R":
            #GPIO.output(self.mux_led_pos[led_pin],GPIO.HIGH)
            GPIO.output(self.mux_led_pos[led_pin],GPIO.LOW)
            os.popen(f"cansend {self.module_name} {id_list}#{payload_list}", 'w', 128)
        if fd_list == "0":
            #GPIO.output(self.mux_led_pos[led_pin],GPIO.HIGH)
            GPIO.output(self.mux_led_pos[led_pin],GPIO.LOW)
            os.popen(f"cansend {self.module_name} {id_list}#{payload_list}", 'w', 128)
        else:
            #GPIO.output(self.mux_led_pos[led_pin],GPIO.HIGH)
            GPIO.output(self.mux_led_pos[led_pin],GPIO.LOW)
            os.popen(f"cansend {self.module_name} {id_list}##{brs_list}{payload_list}", 'w', 128)
            print(f"cansend {self.module_name} {id_list}##{brs_list}{payload_list}")
        
    def mux_led_control_on(self, led_pin: int):
        GPIO.output(self.mux_led_pos[led_pin],GPIO.HIGH)

    def mux_led_control_off(self, led_pin: int):
        GPIO.output(self.mux_led_pos[led_pin],GPIO.LOW)

    def default_led(self, led_pin: int):
        GPIO.output(self.mux_led_pos[led_pin],GPIO.HIGH)

    def dump_log(self, can_receiver):
        os.popen(f"candump {can_receiver} > ../logs/can.log")

    def random_message(self, message, led_pin:int):
        GPIO.output(self.mux_led_pos[led_pin],GPIO.HIGH)
        os.popen(f"cansend {self.module_name} {message}")
        GPIO.output(self.mux_led_pos[led_pin],GPIO.LOW)

    def default_canup(self):
        os.popen(f"sudo ip link set can0 up type can bitrate 1000000  dbitrate 5000000 restart-ms 1000 berr-reporting on fd on", 'w')
        os.popen(f"sudo ip link set can1 up type can bitrate 1000000  dbitrate 5000000 restart-ms 1000 berr-reporting on fd on", 'w')
        os.popen(f"sudo ifconfig can0 txqueuelen 65536", 'w')
        os.popen(f"sudo ifconfig can1 txqueuelen 65536", 'w')

    def default_candump(self):
        os.popen(f"candump can1 > ../logs/can.log", 'w')

    def default_message_func(self):
        os.popen(f"cansend can0 123#1223", 'w')