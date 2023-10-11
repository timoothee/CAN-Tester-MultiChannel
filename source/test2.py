from tkinter import *
import time
import threading

root = Tk()
root.geometry('500x500')
global lb, lb1, lb2

def thread_1():
    _2str = 'abc'
    lb.insert(0, 'Starting Test')
    time.sleep(1)
    for i in range(5):
        lb.delete(0)
        lb.insert(0, _2str)
        _2str += 'bds'
        time.sleep(0.1)

def func():
    global lb, lb1, lb2
    lb1.insert('end', '12345')
    lb2.insert('end', '12345')
    t1 = threading.Thread(target=thread_1, daemon=True)
    t1.start()

def func2():
    if btnoo.get() == 1:
        root.unbind(bt)
        bt.config(relief='raised')
    else:
        bt.bind(bt)
        bt.config(relief='flat')

btnoo = IntVar()

lb = Listbox(root, bg='black', fg='white', activestyle='underline', disabledforeground='white')
lb.grid(row=0, column=0)
lb.bindtags((lb, root, 'all'))
lb1 = Listbox(root, bg='white', fg='black', activestyle='dotbox',state='disabled', takefocus=0)
lb1.grid(row=1, column=0)
lb2 = Listbox(root, bg='black', fg='white', activestyle='none')
lb2.grid(row=2, column=0)
bt = Button(root, text='Press me', command=func, relief='flat')
bt.grid(row=0, column=1)
chkbt = Checkbutton(root, command=func2, variable=btnoo)
chkbt.grid(row=0, column=2)

root.mainloop()