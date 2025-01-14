'''
Created on Jan 13, 2025

@author: admin
'''
'''
import turtle as t
t.color('red')
t.width(3)
t.speed(0)
radius = 80
for i in range(12):
    t.circle(radius)
    radius += 8
t.done()


import turtle as t
t.color('red')
t.width(2)
t.speed(0)
for a in range(8):
    radius = 80
    for i in range(12):
        t.circle(radius)
        radius += 8
    t.right(45)
t.done()
'''

import turtle as t
t.bgcolor('black')
t.width(2)
t.speed(0)
colors = ['red', 'green', 'blue', 'lime']
ind = 0
for a in range(8):
    radius = 80
    for i in range(12):
        t.color(colors[ind])
        t.circle(radius)
        radius += 8
        if(ind == 3):
            ind = 0
        else:
            ind += 1
    t.right(45)
t.done()
