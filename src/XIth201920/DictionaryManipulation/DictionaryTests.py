'''
Created on Jan 10, 2020

@author: admin
'''
d1 = {1:10,2:20,3:30}
d2 = {1:40,2:50,3:60}
d3 = {1:70,2:80,3:90}
#d4 = {d1:'a',d2:'b',d3:'c'}

d4 = {'a':d1,'b':d2,'c':d3}
print(d1)
print(d2)
print(d3)
print(d4)

val = d4['a']
print("val - ",val)