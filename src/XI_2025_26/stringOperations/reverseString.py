'''
Created on Jan 15, 2026
Program to read the string and display it in reverse order
@author: admin
'''
st = 'python'
length = len(st)

for i in range(-1, -length-1, -1) :
    print(i,'-',st[i])
    #print(st[i])