'''
Created on Jan 6, 2025

@author: admin
'''
import turtle as t
t.speed(0)
t.width(3)
#to position the cursor on left top
t.penup()
t.goto(-300,300)
t.pendown()

for a in range(4) :
    t.fillcolor('orange')
    t.begin_fill()
    for i in range(8) :
        t.circle(20)
        t.forward(40)
    t.right(90)
    t.end_fill()

for a in range(4) :
    t.fillcolor('blue')
    t.begin_fill()
    for i in range(8) :
        t.circle(-20)
        t.forward(40)
    t.right(90)
    t.end_fill()
t.done()