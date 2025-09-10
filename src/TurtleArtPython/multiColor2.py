'''
Created on Dec 26, 2024

@author: admin
'''
import turtle as tur
tur.bgcolor('white')
tur.color('blue')
tur.speed(0)
colors = ['red','green','blue','yellow','pink']
a = 0
for j in range(20) :
    if a > 4 :
        a = 0
    tur.fillcolor(colors[a])
    tur.begin_fill()
    for i in range(3):
        tur.forward(200)
        tur.right(120)
    tur.right(20)
    tur.end_fill()
    a = a+1
tur.done()