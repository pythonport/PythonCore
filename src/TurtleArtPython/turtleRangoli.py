'''
Created on Jan 13, 2025

@author: admin
'''
import turtle as t
t.color('blue')
t.width(4)
t.speed(0)
for a in range(25):
    for i in range(4):
        t.forward(100)
        t.right(90)
    t.right(25)
t.done()