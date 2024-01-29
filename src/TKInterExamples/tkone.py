'''
Created on Jan 4, 2024

@author: Admin
'''
import tkinter as tk

root = tk.Tk()
root.geometry("300x350")
root.title('JNV Dhanbad')

def sayHello():
    input = eName.get()
    lblout['text'] = ''
    lblout['text'] = "Hello to - {}".format(input)

lblHeader = tk.Label(root, text="Welcome to GUI programming",  font=('Times New Roman', 15, 'bold'))
lblout = tk.Label(root, text="",  font=('Times New Roman', 15, 'bold'))
eName = tk.Entry(root, font=('Times New Roman', 15, 'bold'))
btnHello = tk.Button(root, height=2, width=10, text="Click Me", command=lambda:sayHello())

lblHeader.pack()
eName.pack()
btnHello.pack()
lblout.pack()

tk.mainloop()