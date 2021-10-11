import sys
try :
    from Tkinter import *
except ImportError :
    from tkinter import *
import time

def tick():
    # get the current local time from the PC
    time_string = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    clock.config(text=time_string)
    clock.after(200, tick)

root = Tk()
root.configure(background="green")
root.title("Digital Clock using TKinter")

clock = Label(root, font=('times', 250, 'bold'), bg='orange')
#clock.pack(fill=BOTH, expand=1)
clock.pack()
'''
logo = PhotoImage(file="nvslogo.gif")
logolbl = Label(root, image=logo)
logolbl.pack()
'''
tick()
root.mainloop()