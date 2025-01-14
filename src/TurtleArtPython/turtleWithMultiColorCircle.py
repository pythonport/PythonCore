'''
Created on Jan 14, 2025

@author: admin
'''
import turtle as t
t.color('red')
t.width(2)
t.speed(0)
def morpankh(r):
    radius = r
    colors = ['red', 'green', 'blue', 'lime']
    ind = 0
    for i in range(22):
        t.fillcolor(colors[ind])
        t.begin_fill()
        t.circle(radius)
        t.end_fill()
        radius -= 8
        if(ind == 3):
                ind = 0
        else:
            ind += 1

morpankh(150)
t.done()