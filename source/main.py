'''
from can_frame import CanFrame
from can_module import CanModule
from tkinter import ttk
import os
from splash import SplashScreen
'''
from GUI import *
from interface import *  # for interface test

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

if __name__ == "__main__":
    # MAJOR.MINOR.PATCH
    gui = CANGui("v.1.11.0")
    gui.build()
    #gui.root.overrideredirect(True)
    gui.root.mainloop()
    #itf = InterfaceTest("v.1.10.0")
    #itf.build()
    #itf.root.overrideredirect(True)
    #itf.root.mainloop()
