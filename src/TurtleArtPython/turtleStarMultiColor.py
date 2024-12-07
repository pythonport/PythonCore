'''
Created on Dec 3, 2024

@author: admin
'''
import turtle as tur
import colorsys as cs
tur.speed(0)
tur.width(1)
tur.bgcolor('black')
#tur.color("yellow")
for i in range(50) :
    for j in range(5) :
        tur.color(cs.hsv_to_rgb(i/15,j/25,1))
        tur.forward(200)
        tur.right(144)
    tur.right(10)
tur.done()