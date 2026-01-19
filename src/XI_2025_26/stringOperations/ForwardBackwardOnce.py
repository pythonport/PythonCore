'''
Created on Jan 15, 2026
print forward and backward string together
@author: admin
'''
st = input('Enter string - ')
length = len(st)
a = 0
for i in range(-1, -length-1, -1) :
    print(st[a],st[i])
    a+=1