'''
Created on Mar 2, 2021

@author: admin
'''
name =""
admno = 0
fee = 0.0

def sinput():
    global name 
    global admno 
    global fee 
    name= input("Enter name - ")
    admno= int(input("Enter admno - "))
    fee= float(input("Enter fee - "))

def output():
    print("Student name - ",name)
    print("Student admno - ",admno)
    print("fee is - ",fee)
    
sinput()
output()