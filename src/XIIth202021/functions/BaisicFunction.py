'''
Created on Dec 23, 2020
function basic example
Void
Non-Void
Argument
Parameter
@author: admin
'''


def sayHello(name):  # void function
    print("Hello to you Mr - ", name)
    return


def getSum(x, y): #non-void function
    sum = x + y
    return sum


nm = "Rahul"
sayHello(nm)
val  = sayHello("Arjun")
print("Val is - ",val)

sm = getSum(12,8)
print("Sum value is - ",sm)
