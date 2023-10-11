from tkinter import *
from tkinter.ttk import Progressbar
import time
from tkinter import ttk
import threading
from tkinter.filedialog import asksaveasfile
import random
from PIL import Image, ImageTk
import tkinter as tk
class SplashScreen:
    def __init__(self):
        pass
    def threadfunc(self):
        t1 = threading.Thread(target=self.splash)
        t1.start()

    def splash(self):
        self.root = tk.Tk()
        self.logo_image = Image.open("photo.png").resize((500, 250), Image.ANTIALIAS)
        self.logo_image = ImageTk.PhotoImage(self.logo_image)

        self.root.overrideredirect(True)

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        logo_width = self.logo_image.width()
        logo_height = self.logo_image.height()
        x = (screen_width - logo_width) // 2
        y = (screen_height - logo_height) // 2
        self.root.geometry("+{}+{}".format(x, y))

        self.logo_frame = Frame(self.root)
        self.logo_frame.grid(row=0, column=0, sticky='nsew')

        frame = Frame(self.root)
        frame.grid(row=1, column=0, sticky='nsew')

        self.logo_label = Label(self.logo_frame, image=self.logo_image)
        self.logo_label.grid(row=0, column=0)

        self.progressbar = Progressbar(frame, orient='horizontal', length=200)
        self.progressbar.config()
        self.progressbar.grid(row=0, column=0, padx=5)

        self.text_label = Label(frame, text="...", font=("Arial", 11))
        self.text_label.grid(row=0, column=1, padx=(200,0), sticky='e')

        self.list = ['.modules', 'CAN-HAT.sh' , 'continue', '.install','initialize','continue']

        self.root.update()

        for i in range(200):
            if i % 10 == 0:
                self.abc()
            self.root.update()
            self.progressbar.step(0.5)
            time.sleep(0.01)
        self.destroy()
        self.root.mainloop()

    def abc(self):
        self.text_label.config(text = random.choice(self.list))

    def destroy(self):
        self.root.overrideredirect(False)
        self.root.destroy()
