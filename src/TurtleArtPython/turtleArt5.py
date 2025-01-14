'''
Created on Dec 21, 2024

@author: admin
'''
"""
import turtle as t
t.width(2)
t.bgcolor('black')
t.color("yellow")
for i in range(4):
    t.forward(200)
    t.right(90)
t.done()

import turtle as t
t.width(2)
t.bgcolor('black')
t.color("yellow")
for j in range(10):
    for i in range(4):
        t.forward(200)
        t.right(90)
    t.right(20)
t.done()

import turtle as t
t.width(2)
t.speed(0)
t.bgcolor('black')
t.color("yellow")
for j in range(30):
    t.circle(50)
    t.right(20)
t.done()"""

import turtle as t
t.width(2)
t.speed(0)
t.bgcolor('black')
t.color("yellow")
radius = 50
for j in range(45):
    t.circle(radius)
    t.right(20)
    radius +=2
t.done()