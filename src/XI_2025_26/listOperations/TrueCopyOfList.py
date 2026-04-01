'''
Created on Feb 19, 2026

@author: admin
'''

a = [1,2,3]
print('original a -',a)
b = list(a)  #by using list function
b[2]=334
print('a -',a)
print('b - ',b)

c = [11,22,33]
print('original c -',c)
d = c.copy()  #by using copy function
c[2]=555
print('c -',c)
print('d - ',d)

e = [66,55,44]
f = e[:]   #by assigning list slicing to another variable
print(e)
print(f)
f[2]=144
print(e)
print(f)
