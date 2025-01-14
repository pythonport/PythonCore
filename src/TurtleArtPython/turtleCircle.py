'''
Created on Dec 13, 2024

@author: admin
'''
import turtle as tur
tur.setup(800,800)
tur.speed(2)
tur.tracer(10)
tur.width(1)
tur.bgcolor('black')
tur.color('yellow')
for i in range(1, 150, 5) :
    tur.circle(20+i)
    tur.circle(-20-i)
    tur.right(5)
tur.done()