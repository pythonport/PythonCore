'''
Created on Dec 26, 2024

@author: admin
'''
import turtle as tur
tur.bgcolor('black')
tur.color('white')
tur.speed(0)
tur.fillcolor('green')
tur.begin_fill()
r = 100
for j in range(20) :
    r = r-5
    tur.circle(r)
    tur.right(20)
tur.end_fill()
tur.done()