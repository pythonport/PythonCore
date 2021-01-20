'''
Created on Dec 17, 2020
Use of global keyword.
@author: admin
'''
a = 90  #Global Variable

def globalUse() :
    global a  #global keyword
    a = 10   #Local Variable
    print("a from function - ", a)
    print("ID line no 12 of a -", id(a))


print("a outside function - ", a)
print("ID line no 16 of a -", id(a))
globalUse()
print("a outside function - ", a)
print("ID line no 19  a -", id(a))
