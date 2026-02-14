'''
Created on Feb 9, 2026

@author: admin
'''
a = 'python'
for i in a :
    print(i,i)
    
    
for i in range(len(a)) :
    print(i,'-',a[i])
    
for i in range(-1, -len(a)-1,-1) :
    print(i,'-',a[i])
    
print('Py'+'python')
print('55'+'55')
print(55+55)
print('**'*5)
print(6*'==')

#string slicing
print(a[1:4])
print(a[1:14])
print(a[::]) #whole string forward direction
print(a[::-1]) #whole string backward direction
print(a[::2]) #String slice with gap of 2

num = 1
while num<=20:
    print('square of', num,' - ',num**2)
    num+=2
    
num = 5
while num<=50:
    print(num)
    num+=5