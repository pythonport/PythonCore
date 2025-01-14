'''
Created on Jan 6, 2025

@author: admin
'''
import turtle as t
t.speed(0)
t.width(4)
#positioning
t.penup()
t.backward(300)
t.left(90)
t.forward(150)
t.right(90)
t.pendown()

def downTriangle(a):
    for i in range(4):
        t.fillcolor('green')
        t.begin_fill()
        for j in range(a):
            t.forward(50)
            t.right(120)
            t.forward(50)
            t.right(120)
            t.forward(50)
            t.right(120)
            t.forward(50)
        t.end_fill()
        t.right(90)
        
def upTriangle(a):   
    for i in range(4):
        t.fillcolor('orange')
        t.begin_fill()
        for j in range(a):
            t.forward(50)
            t.left(120)
            t.forward(50)
            t.left(120)
            t.forward(50)
            t.left(120)
            t.forward(50)
        t.end_fill()
        t.right(90)

downTriangle(10)
upTriangle(10)
t.done()