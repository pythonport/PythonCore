'''
Created on Dec 26, 2024

@author: admin
'''
import turtle as tur
tur.bgcolor('black')
tur.color('white')
tur.speed(0)
for j in range(20) :
    tur.fillcolor('blue')
    tur.begin_fill()
    for i in range(3):
        tur.forward(200)
        tur.right(120)
    tur.right(20)
    tur.end_fill()
tur.done()