from tkinter import *
import os
import platform
import threading
import time
from PIL import Image, ImageTk
import subprocess
from tkinter import font

class InterfaceTest():
    def __init__(self, gui_revision: str):
        self.gui_revision = gui_revision
        self.root = Tk()
        self.root.wm_attributes('-type', 'splash')
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        #self.root.title(f"CanInterfaceGUI {self.gui_revision}")

        self.menu_bar = Menu(self.root, bg="grey")
        self.general = Menu(self.menu_bar, tearoff = 0, activebackground='#7f7e7f', activeborderwidth=0)
        self.view = Menu(self.menu_bar, tearoff = 0)
        self.help = Menu(self.menu_bar, tearoff = 0)
        self.blankenu = Menu(self.menu_bar, tearoff=0)
        self.canrasp = Menu(self.menu_bar, tearoff=0)

        self.ico = PhotoImage(file="/home/raspberry/CAN-Tester/images/button.png")

        self.general.add_command(label="About CANrasp")
        self.general.add_command(label="Check for Updates...")
        self.general.add_separator()
        self.cpu_sensor = Menu(self.general, tearoff=0)
        self.general.add_cascade(label="Sensors")
        self.general.add_separator()
        self.general.add_command(label="Quit", command=self.root.destroy)
        self.enable_menu = Menu(self.canrasp, tearoff=0)

        self.view.add_command(label="Vertical")
        self.view.add_command(label="Horizontal")
        self.help.add_command(label="Welcome")
        self.help.add_command(label="Contact")
        self.canrasp.add_cascade(label='Enable', menu=self.enable_menu)
        self.enable_menu.add_command(label ='thickness 2', command=self.frame_enable2)
        self.enable_menu.add_command(label ='thickness 3', command=self.frame_enable3)
        self.canrasp.add_command(label='Disable', command=self.frame_disable)

        self.menu_bar.add_cascade(label="General", menu=self.general, activebackground='#7f7e7f')
        self.menu_bar.add_cascade(label="View", menu=self.view)
        self.menu_bar.add_cascade(label="Help", menu=self.help)
        self.menu_bar.add_cascade(label="".ljust(172))
        self.menu_bar.add_cascade(label=(f"CanInterfaceGUI {self.gui_revision}"), menu=self.canrasp)
        self.menu_bar.add_cascade(label="".ljust(206))
        self.menu_bar.entryconfig("".ljust(172),state='disabled')
        self.menu_bar.entryconfig((f"CanInterfaceGUI {self.gui_revision}"),state='normal')
        self.menu_bar.entryconfig("".ljust(206),state='disabled')
        
        self.menu_bar.add_command(label="_", activebackground='yellow', command=self.minimize(), font=font.Font(weight="bold"))
        self.menu_bar.add_command(label="x", activebackground='red', command=self.root.destroy, font=font.Font(weight="bold"))

        self.root.config(menu=self.menu_bar)
        self.brs_box = IntVar()
        self.ext_box = IntVar()
        self.id_text = StringVar()
        self.RTR_box = IntVar()
        self.FD_box = IntVar()
        self.que_loop_var = IntVar()
        self.payload_entry = StringVar()
        self.payload_entry.set("")
        self.can_sender_var = StringVar()
        self.can_sender_var.set('Select')
        self.can_receiver_var = StringVar()
        self.can_receiver_var.set('Select')
        self.drop_down_id_baudrate_var = StringVar()
        self.drop_down_id_baudrate_var.set("Select")
        self.drop_down_data_baudrate_var = StringVar()
        self.drop_down_data_baudrate_var.set("Select")
        self.see_only_dropdown_var = StringVar()
        self.see_only_dropdown_var.set('Test')
        self.see_only_dropdown_list = ('Echo', 'Negate', 'Increment', 'Decrement')
        self.text_variable_sp = StringVar()
        self.text_variable_sp.set("N/A")
        self.dtext_variable_sp = StringVar()
        self.position = 0
        self.can_send_module_optionmenu = None
        self.can_receive_module_optionmenu = None
        self.can_send_module_optionmenu = ("CAN0", "CAN1")
        self.can_receive_module_optionmenu = ("CAN0","CAN1")
        self.can_dict = {'CAN0':"can0", 'CAN1':"can1", 'CAN2':"can2"}
        self.baudrate_list = ('100K','200K','400K','500K','1M')
        self.data_baudrate_list = ('100K','200K','400K','500K','1M','2M','3M','4M','5M','6M','7M','8M')
        self.baudrate_dict = {'100K':100000,'200K':200000,'400K':400000,'500K':500000,"1M":1000000,"2M":2000000,'3M':3000000,'4M':4000000,"5M":5000000,"6M":6000000,"7M":7000000,"8M":8000000}   
        self.can_frame_changed = False
        self.program_running = True
        self.chg_var = 0
        self.chg_var1 = 0
        self.list_read = []
        self.list_mem = []
        self.thread_error = False
        self.cpu_temp = '0'
        self.dmessage = StringVar()
        self.dev_status = False
        self.root_dev = None
        self.delay_entry_var = IntVar()
        self.delay_optionmenu = ("1s","2s","3s","5s")
        self.delay_optionmenu_dict = {'1s':1, '2s':2, '3s':3, '5s':5}
        self.messages_loop_var = IntVar()
        self.loop_active = False
        self.active_loop_var = False
        self.stop_ran_func_var = False
        t4 = threading.Thread(target=self.sensor_temp, daemon=True)
        t4.start()
        t5 = threading.Thread(target=self.temp_var_color, daemon=True)
        t5.start()
        self.test_mode1 = StringVar()
        self.negate = StringVar()
        self.increment = StringVar()
        self.decrement = StringVar()
        self.frame_color = 'red'
        self.can0_ckBox_var = IntVar()
        self.can1_ckBox_var = IntVar()
        self.can2_ckBox_var = IntVar()
        self.can3_ckBox_var = IntVar()
        self.can4_ckBox_var = IntVar()
        self.can5_ckBox_var = IntVar()
        self.can6_ckBox_var = IntVar()
        self.can7_ckBox_var = IntVar()
        self.mux_list = [self.can0_ckBox_var, self.can1_ckBox_var, self.can2_ckBox_var, self.can3_ckBox_var, self.can4_ckBox_var, self.can5_ckBox_var, self.can6_ckBox_var, self.can7_ckBox_var]
        self.mux_sel = [23, 16, 7]

    def build(self):
        #self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.can_frame1 = Frame(self.root, highlightbackground='grey', highlightthickness=3)
        self.can_frame1.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        self.can_frame2 = Frame(self.root, highlightbackground='grey', highlightthickness=3)
        self.can_frame2.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        self.can_frame3 = Frame(self.root,  highlightbackground='light grey', highlightthickness=3)
        self.can_frame3.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
        
        self.can_frame4 = Frame(self.root, highlightbackground='grey', highlightthickness=3)
        self.can_frame4.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)
        
        self.can_frame5 = Frame(self.root, highlightbackground='#a9a9a9', highlightthickness=3)
        self.can_frame5.grid(row=6, column=0, sticky="nsew", pady=5, padx=5)

        self.can_frame6= Frame(self.root, highlightbackground='light grey', highlightthickness=3)
        self.can_frame6.grid(row=2, column=1, padx=5, pady=5)
        
        self.can_frame7 = Frame(self.root, highlightbackground='grey', highlightthickness=3)
        self.can_frame7.grid(row=3, column=1, sticky="w", padx=5, pady=5)

        # Mux label has no frame, row 5 column 0 are reserved
        self.can_frame8 = Frame(self.root, highlightbackground='grey', highlightthickness=3)
        self.can_frame8.grid(row=7, column=0, sticky='w', padx=5)

        self.can_frame8_1 = Frame(self.can_frame8)
        self.can_frame8_1.grid(row=0, column=0, padx=(10,0))
        
        self.can_frame8_2 = Frame(self.can_frame8)
        self.can_frame8_2.grid(row=0, column=1, sticky='n')

        self.empty_can_frame1 = Frame(self.root)
        self.empty_can_frame1.grid(row=0, column=1, padx=20, sticky='e')
        
        # frame 1
        self.can_interface_sender_label = Label(self.can_frame1, text = "CAN SENDER")
        self.can_interface_sender_label.grid(row=0, column=0, pady=(20,0))

        self.sender_drop_down_menu = OptionMenu(self.can_frame1, self.can_sender_var, *self.can_send_module_optionmenu)
        self.sender_drop_down_menu.config(width=5)
        self.sender_drop_down_menu.grid(row = 1, column = 0)

        self.can_interface_receiver_label = Label(self.can_frame1, text = "CAN RECEIVER")
        self.can_interface_receiver_label.grid(row=2, column=0)

        self.receiver_drop_down_menu = OptionMenu(self.can_frame1, self.can_receiver_var, *self.can_receive_module_optionmenu)
        self.receiver_drop_down_menu.config(width=5)
        self.receiver_drop_down_menu.grid(row = 3, column = 0)

        self.id_baudrate_Label = Label(self.can_frame1, text = "ID Baudrate")
        self.id_baudrate_Label.grid(row=0, column=1, pady=(20,0))

        self.drop_down_id_baudrate = OptionMenu(self.can_frame1,  self.drop_down_id_baudrate_var, *self.baudrate_list)
        self.drop_down_id_baudrate.config(width=5)
        self.drop_down_id_baudrate.grid(row = 1, column=1)

        self.data_baudrate_Label = Label(self.can_frame1, text = "DATA Baudrate")
        self.data_baudrate_Label.grid(row=0, column=2, pady=(20,0), padx=(0,20))

        self.drop_down_data_baudrate = OptionMenu(self.can_frame1, self.drop_down_data_baudrate_var, *self.data_baudrate_list)
        self.drop_down_data_baudrate.config(width=5)
        self.drop_down_data_baudrate.grid(row = 1, column=2, padx=(0,20))

        self.temp_cpu_label= Label(self.can_frame1, text= self.cpu_temp, width=15)
        self.temp_cpu_label.grid(row=3, column=1)

        self.sample_point_label = Label(self.can_frame1, text = "ID SP")
        self.sample_point_label.config(state='disabled')
        self.sample_point_label.grid(row=0, column=3, pady=(20,0))

        self.empty_label = Label(self.can_frame1,text='   ')
        self.empty_label.grid(row=0, column=4)

        self.dsample_point_label = Label(self.can_frame1, text = "DATA SP")
        self.dsample_point_label.grid(row=0, column=5, pady=(20,0))

        self.sample_point_entry = Entry(self.can_frame1, textvariable = self.text_variable_sp)
        self.sample_point_entry.config(width=5, state='disable')
        self.sample_point_entry.grid(row=1, column=3)

        self.dsample_point_entry = Entry(self.can_frame1, textvariable = self.dtext_variable_sp)
        self.dsample_point_entry.config(width=5)
        self.dsample_point_entry.grid(row=1, column=5)

        self.actual_data_label = Label(self.can_frame1, text="Actual Data", font=('Arial', 10))
        self.actual_data_label.config(state='disabled')
        self.actual_data_label.grid(row=2, column=3, padx=(0,35))

        self.sample_point_data = Label(self.can_frame1, text = "0.750", font=('Arial', 10))
        self.sample_point_data.config(state='disabled')
        self.sample_point_data.grid(row=2, column=3, sticky='e')

        self.actual_data_dlabel = Label(self.can_frame1, text="Actual Data", font=('Arial', 10))
        self.actual_data_dlabel.grid(row=2, column=5, padx=(0,35))

        self.sample_dpoint_data = Label(self.can_frame1, text = "0.750", font=('Arial', 10))
        self.sample_dpoint_data.grid(row=2, column=5, sticky='e')

        self.empty_label2 = Label(self.can_frame1, text='   ')
        self.empty_label2.grid(row=0, column=6, padx=(107,0))

        self.status_label = Label(self.can_frame1, text="STATUS")
        self.status_label.grid(row=0, column=7, pady=(20,0))

        self.up_down_button = Button(self.can_frame1, text="UP",fg="green", width=3, state="disabled")
        self.up_down_button.grid(row=0, column=8, sticky='e', padx=(5,0), pady= (10,0))

        self.default_status_label = Label(self.can_frame1, text="DOWN", fg='red')
        self.default_status_label.config(width=5)
        self.default_status_label.grid(row=1, column=7)
        
        self.dev_button = Button(self.can_frame1, text= "<  >", width=3)
        self.dev_button.grid(row=1, column=8, padx=(10,0))

        self.empty_label2 = Label(self.can_frame1, text=' ')
        self.empty_label2.grid(row=0, column=9, padx=(5,0))
        
        # frame 2
        self.RTR_Label = Label(self.can_frame2, text="RTR")
        self.RTR_Label.grid(row= 0, column =0, padx=(20,0))

        self.RTR_CkBtn = Checkbutton(self.can_frame2, variable=self.RTR_box)
        self.RTR_CkBtn.grid(row = 1, column=0, padx=(20,0))

        self.brs_Label = Label(self.can_frame2, text="BRS")
        self.brs_Label.config(state='disable')
        self.brs_Label.grid(row= 0, column =1)

        self.brs_CkBt = Checkbutton(self.can_frame2, variable=self.brs_box)
        self.brs_CkBt.config(state='disable')
        self.brs_CkBt.grid(row = 1, column=1)

        self.ext_flag_Label = Label(self.can_frame2, text="EXT")
        self.ext_flag_Label.grid(row =0 ,column=2)

        self.ext_flag_CkBt = Checkbutton(self.can_frame2, variable=self.ext_box)
        self.ext_flag_CkBt.grid(row=1, column=2)

        self.ext_flag_Label = Label(self.can_frame2, text="FD")
        self.ext_flag_Label.grid(row= 0, column=3)

        self.FD_CkBtn = Checkbutton(self.can_frame2, variable=self.FD_box)
        self.FD_CkBtn.grid(row = 1, column=3)

        self.frame_id_Label = Label(self.can_frame2, text="ID (0x)")
        self.frame_id_Label.grid(row = 0, column=4, padx=(5,0), sticky='w')
        self.default_label_color = self.frame_id_Label.cget('fg')

        self.frame_id_entry = Entry(self.can_frame2, textvariable=self.id_text, width= 10)
        self.frame_id_entry.grid(row = 1, column=4, padx=(5,0))
        self.default_entry_color = self.frame_id_entry.cget('fg')

        self.payload_Label = Label(self.can_frame2, text="PAYLOAD")
        self.payload_Label.grid(row = 0, column=5, sticky='w')

        self.payload_Entry = Entry(self.can_frame2, textvariable=self.payload_entry)
        self.payload_Entry.grid(row = 1, column=5)

        self.root.update()

        self.add_to_q = Button(self.can_frame2, text="ADD TO QUE", width=10)
        self.add_to_q.grid(row = 1, column=6, padx=(292,0), pady=(0,5))

        # frame 3
        self.que_listbox_label = Label(self.can_frame3, text = "Message list")
        self.que_listbox_label.grid(row=0, column=0, sticky='w', padx=(5,0))
        self.que_listbox_label.config(font=('Helvetica bold', 13))
    
        self.que_listbox = Listbox(self.can_frame3, yscrollcommand = 1, width = 92, height= 15,selectmode=EXTENDED)
        self.que_listbox.grid(row=1, column=0, padx=(5,0))

        # frame 4
        self.import_button = Button(self.can_frame4, text="Import")
        self.import_button.grid(row=0, column=0, padx=(5,0))

        self.save_button_input = Button(self.can_frame4, text="Save", command = lambda:self.save("input"))
        self.save_button_input.grid(row=0, column=1)

        self.clear_button_input = Button(self.can_frame4, text="Clear")
        self.clear_button_input.grid(row=0, column=2)

        self.Edit_button = Button(self.can_frame4, text="Edit")
        self.Edit_button.grid(row=0, column=3, padx=(30,0))

        self.ok_button = Button(self.can_frame4, text= "OK")
        self.ok_button.grid(row=0, column=4)

        self.loop_checkbox_label = Label(self.can_frame4, text="LOOP")
        self.loop_checkbox_label.grid(row = 0, column=5, padx=(337,0))

        self.loop_checkbox = Checkbutton(self.can_frame4, variable= self.que_loop_var)
        self.loop_checkbox.grid(row = 0, column=6)

        self.send_button = Button(self.can_frame4, text="SEND QUE")
        self.send_button.grid(row = 0, column=7, pady=5)

        # This widget is not included in frame
        self.mux_label = Label(self.root, text='MUX AREA', font=('Helvetica bold', 13))
        self.mux_label.grid(row=5, column=0, padx=(22,0), pady=(5,0), sticky='w')
        
        # frame 5
        self.can0_ckBox = Checkbutton(self.can_frame5, variable = self.can0_ckBox_var, state='disable')
        self.can0_ckBox.grid(row=1, column=0, padx=(15,0))
        self.can0_ckBox.select()

        self.can0_label = Label(self.can_frame5, text='CAN 0')
        self.can0_label.grid(row=2, column=0, padx=(15,0))

        self.can1_ckBox = Checkbutton(self.can_frame5, variable = self.can1_ckBox_var)
        self.can1_ckBox.grid(row=1, column=1, padx=(10,0))

        self.can1_label = Label(self.can_frame5, text='CAN 1')
        self.can1_label.grid(row=2, column=1, padx=(10,0))

        self.can2_ckBox = Checkbutton(self.can_frame5, variable = self.can2_ckBox_var)
        self.can2_ckBox.grid(row=1, column=2, padx=(10,0))

        self.can2_label = Label(self.can_frame5, text='CAN 2')
        self.can2_label.grid(row=2, column=2, padx=(10,0))

        self.can3_ckBox = Checkbutton(self.can_frame5, variable = self.can3_ckBox_var)
        self.can3_ckBox.grid(row=1, column=3, padx=(10,0))

        self.can3_label = Label(self.can_frame5, text='CAN 3')
        self.can3_label.grid(row=2, column=3, padx=(10,0))

        self.can4_ckBox = Checkbutton(self.can_frame5, variable = self.can4_ckBox_var)
        self.can4_ckBox.grid(row=1, column=4, padx=(10,0))

        self.can4_label = Label(self.can_frame5, text='CAN 4')
        self.can4_label.grid(row=2, column=4, padx=(10,0))

        self.can5_ckBox = Checkbutton(self.can_frame5, variable = self.can5_ckBox_var)
        self.can5_ckBox.grid(row=1, column=5, padx=(10,0))

        self.can5_label = Label(self.can_frame5, text='CAN 5')
        self.can5_label.grid(row=2, column=5, padx=(10,0))

        self.can6_ckBox = Checkbutton(self.can_frame5, variable = self.can6_ckBox_var)
        self.can6_ckBox.grid(row=1, column=6, padx=(10,0))

        self.can6_label = Label(self.can_frame5, text='CAN 6')
        self.can6_label.grid(row=2, column=6, padx=(10,0))

        self.can7_ckBox = Checkbutton(self.can_frame5, variable = self.can7_ckBox_var)
        self.can7_ckBox.grid(row=1, column=7, padx=(10,0))

        self.can7_label = Label(self.can_frame5, text='CAN 7')
        self.can7_label.grid(row=2, column=7, padx=(10,0))
        
        # frame 6
        self.can_bus_listbox_label = Label(self.can_frame6, text="CAN BUS")
        self.can_bus_listbox_label.grid(row=0, column=0, sticky='w', padx=10)
        self.can_bus_listbox_label.config(font=('Helvetica bold', 13))

        self.can_bus_listbox = Listbox(self.can_frame6, yscrollcommand = 1, width = 85, height=15, selectmode =EXTENDED)
        self.can_bus_listbox.grid(row=1, column=0, padx=10)

        # frame 7
        self.save_button_output = Button(self.can_frame7, text="Save", command=lambda:self.save("output"))
        self.save_button_output.grid(row=0, column=0, sticky='w', padx=10, pady=5)

        self.clear_button_output = Button(self.can_frame7, text="Clear")
        self.clear_button_output.grid(row=0, column=1, sticky='w')
        
        self.can_bus_seeonly_optionemnu = OptionMenu(self.can_frame7, self.see_only_dropdown_var, *self.see_only_dropdown_list)
        self.can_bus_seeonly_optionemnu.config(width = 6, state='normal')
        self.can_bus_seeonly_optionemnu.grid(row=0, column=2, sticky='w')

        self.start_test_button = Button(self.can_frame7, text="Start Test")
        self.start_test_button.grid(row=0, column=3, sticky='w', padx=(0,10))

        self.start_thread_label = Label(self.can_frame7, text='Start Thread')
        self.start_thread_label.grid(row=0, column=4, sticky='e', padx=(335,0))

        self.start_thread_ckbt = Checkbutton(self.can_frame7)
        self.start_thread_ckbt.grid(row=0, column=5, padx=(0,10))
        
        # frame 8_1
        self.info_listbox_label = Label(self.can_frame8_1, text='Info list')
        self.info_listbox_label.grid(row=0, column=0, sticky='w', pady=(5,0))
        self.info_listbox_label.config(font=('Helvetica bold', 13))

        self.info_listbox =Listbox(self.can_frame8_1, width = 50, height=7, selectmode=EXTENDED)
        self.info_listbox.grid(row=1, column= 0, pady=5)

        self.ep_label = Label(self.can_frame8_1, text='  ')
        self.ep_label.grid(row=0, column=1, padx=(20,0))
        
        # frame 8_2
        self.loop_section_label = Label(self.can_frame8_2, text='RANDOM LOOP SECTION')
        self.loop_section_label.grid(row=0, column=0, pady=(10,0))
        self.loop_section_label.config(font=('Helvetica bold', 13))
        
        self.delay_label = Label(self.can_frame8_2, text="DELAY (ms)")
        self.delay_label.grid(row=1, column=0, padx=(25,0), sticky='w')

        self.loop_msg_label = Label(self.can_frame8_2, text="MESSAGES")
        self.loop_msg_label.grid(row=1, column=0, padx=(0,25), sticky='e')

        self.delay_entry = Entry(self.can_frame8_2, textvariable=self.delay_entry_var)
        self.delay_entry.config(width=6)
        self.delay_entry.grid(row=2, column=0, padx=(30,0), sticky='w')

        self.loop_messages_entry = Entry(self.can_frame8_2, textvariable=self.messages_loop_var)
        self.loop_messages_entry.config(width=6)
        self.loop_messages_entry.grid(row=2, column=0, padx=(0,30), sticky='e')

        self.loop_start_button = Button(self.can_frame8_2, text="START", width=5)
        self.loop_start_button.grid(row=3, column=0, padx=(25,0), sticky='w')

        self.loop_stop_button = Button(self.can_frame8_2, text="STOP", width=5)
        self.loop_stop_button.grid(row=3, column=0, padx=(0,25), sticky='e')

        self.emp = Label(self.can_frame8_2, text='  ')
        self.emp.grid(row=0, column=1)

        #This widgets are not included in a frame
        self.icsolution_label = Label(self.root, text='Powered by: ICSolution', font='Helvetica 11 bold')
        self.icsolution_label.grid(row=8, column=0, sticky='w', padx=(10,0), pady=(60,0))
        
        self.mail_label = Label(self.root, text='timotei.sandru@continental-corporation.com', font='Helvetica 11 bold')
        self.mail_label.grid(row=9, column=0, sticky='w', padx=(10,0), pady=(7,0))
        
        # frame 12
        try:
            self.image_dimenion = PhotoImage(file="/home/raspberry/CAN-Tester/images/Continental-Logo.png")
            continental_logo_width, continental_logo_height = self.image_dimenion.width(), self.image_dimenion.height()
            self.imagee = Image.open(r"/home/raspberry/CAN-Tester/images/Continental-Logo.png").resize((continental_logo_width+130, continental_logo_height+30), Image.ANTIALIAS)
            self.imagee = ImageTk.PhotoImage(self.imagee)
            self.label1 = Label(self.empty_can_frame1, image= self.imagee)
            self.label1.grid(row=0, column=0)
        except:
            self.label1 = Label(self.empty_can_frame1, text= 'Missing Continental Logo Image\nPlease contact developer,git\nbelow you can find e-mail address')
            self.label1.grid(row=0, column=0, padx=50, pady=(50,0))
    
    def minimize(self):
        self.root.state(newstate='iconic')

    def frame_disable(self):
        self.can_frame1.config(highlightthickness=0)
        self.can_frame2.config(highlightthickness=0)
        self.can_frame3.config(highlightthickness=0)
        self.can_frame4.config(highlightthickness=0)
        self.can_frame5.config(highlightthickness=0)
        self.can_frame6.config(highlightthickness=0)
        self.can_frame7.config(highlightthickness=0)
        self.can_frame8.config(highlightthickness=0)
    
    def frame_enable2(self):
        self.can_frame1.config(highlightthickness=2)
        self.can_frame2.config(highlightthickness=2)
        self.can_frame3.config(highlightthickness=2)
        self.can_frame4.config(highlightthickness=2)
        self.can_frame5.config(highlightthickness=2)
        self.can_frame6.config(highlightthickness=2)
        self.can_frame7.config(highlightthickness=2)
        self.can_frame8.config(highlightthickness=2)

    def frame_enable3(self):
        self.can_frame1.config(highlightthickness=3)
        self.can_frame2.config(highlightthickness=3)
        self.can_frame3.config(highlightthickness=3)
        self.can_frame4.config(highlightthickness=3)
        self.can_frame5.config(highlightthickness=3)
        self.can_frame6.config(highlightthickness=3)
        self.can_frame7.config(highlightthickness=3)
        self.can_frame8.config(highlightthickness=3)
        
    def sensor_temp(self):
        time.sleep(0.5)
        self.cpu_sensor.add_command(label="CPU")
        output = subprocess.check_output(['sensors'])
        if output.decode().split('\n')[2].split()[1] == 'N/A':
            x = 6
        else:
            x = 2
        while True:
            output = subprocess.check_output(['sensors'])
            self.temp_int = output.decode().split('\n')[x].split()[1]
            self.cpu_temp = "CPU "+ self.temp_int
            self.cpu_sensor.entryconfig(0,label=self.cpu_temp)
            self.temp_cpu_label.config(text='Temp '+self.cpu_temp)
            time.sleep(0.5)

    def temp_var_color(self):
        time.sleep(5)
        while True:
            temp_int = self.temp_int
            for char in temp_int:
                if char.isdigit() != True:
                    temp_int = temp_int.replace(char, '')
            temp_int = int(temp_int) / 10

            if int(temp_int) < 50:
                self.temp_cpu_label.config(fg=self.default_label_color)
            if int(temp_int) >= 50:
                self.temp_cpu_label.config(fg='#E39010')
            if int(temp_int) > 70:
                self.temp_cpu_label.config(fg='red')