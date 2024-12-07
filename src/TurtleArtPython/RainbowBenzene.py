'''
Created on Dec 3, 2024

@author: admin
'''
# Python program to draw  
# Rainbow Benzene 
# using Turtle Programming 
import turtle as tur
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
tur.speed(0)
tur.bgcolor('black') 
for x in range(360): 
    tur.pencolor(colors[x%6]) 
    tur.width(x//100 + 1) 
    tur.forward(x) 
    tur.left(59) 
tur.hideturtle()
tur.done()