'''
Created on Apr 21, 2026

@author: admin
'''
import turtle
t = turtle.Turtle()
t.width(5)

def makeRactangle():
    t.fd(150)
    t.rt(90)
    t.fd(100)
    t.rt(90)
    t.fd(150)
    t.rt(90)
    t.fd(100)
    #t.right(90)
    t.bk(33)
    t.rt(90)
    t.fd(150)
    t.rt(90)
    t.fd(33)
    t.rt(90)
    t.fd(150)
    t.bk(75)
    t.circle(16)
    t.lt(90)
    t.fd(250)

makeRactangle()
turtle.done()