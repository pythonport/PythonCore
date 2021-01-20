'''
Created on Jul 12, 2019
Code to generate Digital Clock using tkinter api
@author: admin@pythonport.com
'''
from tkinter import *
import time


def tick():
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    clock.after(200, tick)


root = Tk()
# root.configure(background="green")
root.title("Digital Clock using TKinter")

clock = Label(root, font=('times', 100, 'bold',), background='pink', foreground='blue')
clock.pack()
tick()
root.mainloop()
