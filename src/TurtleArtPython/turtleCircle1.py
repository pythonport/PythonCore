'''
Created on Jan 13, 2025

@author: admin
'''
import turtle as t
t.color('green')
t.width(3)
t.speed(0)
side = 100
t.penup()
t.goto(t.pos() + (-250, 250))
t.pendown()
for a in range(10):
  for i in range(4):
    t.forward(side)
    t.right(90)
  t.penup()
  # t.right(25)
  t.goto(t.pos() + (15, -15))
  t.pendown()
  side += 5
t.done()
