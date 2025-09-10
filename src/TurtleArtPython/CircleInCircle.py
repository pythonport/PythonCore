'''
Created on Jul 26, 2025

@author: admin
'''
import turtle
import random
t = turtle.Turtle()
t.speed(0)
t.width(3)
t.color('blue')
radius = 200
lst=["red","green","orange", "yellow","pink","brown","green"]
for i in range(10): 
    #t.fillcolor('lst[random.randint(0,6)]')
    hexColor = str(random.randint(100000,999999))
    t.fillcolor('#'+hexColor)
    t.begin_fill()
    t.circle(radius)
    t.penup()
    t.left(90)
    t.forward(20)
    t.right(90)
    t.pendown()
    t.end_fill()
    radius -= 20
turtle.done()