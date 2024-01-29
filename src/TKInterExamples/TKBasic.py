'''
Created on Jan 3, 2024

@author: Admin
'''
from tkinter import *
import random

root = Tk()
root.geometry("300x250")
root.title('JNV Dhanbad')

num1 = random.randint(1, 10)
num2 = random.randint(2,11)


def take_input():
    input = inputbox.get('1.0', 'end-1c')
    # print(input)
    ans = str(num1 * num2)
    if input == ans:
        lblout['text'] = ("Correct")
    else:
        lblout['text'] = ("Wrong Answer ({})".format(ans))
    calcbutton["state"] = DISABLED


def reset_data():
    for widget in root.winfo_children():
        if isinstance(widget, Entry):  # If this is an Entry widget class
            widget.delete(0, 'end')  # delete all entries 
        if isinstance(widget, Text):
            widget.delete('1.0', 'end')  # Delete from position 0 till end 
        if isinstance(widget, Label):
            lblin['text'] = ""  # Delete from position 0 till end 
            lblout['text'] = ""
        new_Question()
        calcbutton["state"] = NORMAL

def new_Question() :
    global num1
    global num2
    num1 = random.randint(1, 10)
    num2 = random.randint(2,11)
    lblin['text'] ='What is {} * {} = ?'.format(num1, num2)


lblin = Label(text='What is {} * {} = ?'.format(num1, num2),  font=('Times New Roman', 15, 'bold'))
inputbox = Text(root, height=2, width=25, bg='pink',  font=('Times New Roman', 15, 'bold'))
lblout = Label(root, text="",  font=('Times New Roman', 15, 'bold'))

calcbutton = Button(root, height=2, width=10, text="Calculate", command=lambda:take_input())
resetbtn = Button(root, text='Reset', font=22, bg='lightpink', command=lambda:reset_data())

lblin.pack()
inputbox.pack()
lblout.pack()
calcbutton.pack()
resetbtn.pack()

mainloop()    
