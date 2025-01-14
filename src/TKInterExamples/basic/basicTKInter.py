'''
Created on Dec 13, 2024

@author: admin
'''
from tkinter import *

root = Tk()
root.geometry("300x250")
root.title('JNV Dhanbad')

def take_input():
    input = inputbox.get('1.0', 'end-1c')
    lblout['text'] = ("Your name is - ".format(input))



lblname = Label(root, text="Name",  font=('Times New Roman', 15, 'bold'))
inputbox = Text(root, height=2, width=25, bg='pink',  font=('Times New Roman', 15, 'bold'))
lblout = Label(root, text="",  font=('Times New Roman', 15, 'bold'))
calcbutton = Button(root, height=2, width=10, text="Submit", command=lambda:take_input())

lblname.pack()
inputbox.pack()
calcbutton.pack()
lblout.pack()
mainloop()  