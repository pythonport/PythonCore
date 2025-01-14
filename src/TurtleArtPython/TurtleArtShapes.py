'''
Created on Dec 27, 2024

@author: admin
'''
import turtle as t
t.bgcolor('black')
t.color('yellow')
t.speed(0)
t.width(4)

def createTriangle(a):
    for i in range(3):
        t.forward(a)
        t.right(120)

for x in range(25) :
    createTriangle(225)
    t.right(15)

t.color('lime')    
for i in range(20) :
    t.circle(75)
    t.right(20)

t.done()