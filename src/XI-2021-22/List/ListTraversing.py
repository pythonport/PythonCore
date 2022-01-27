'''
Created on Jan 27, 2022

@author: admin
'''
lst = ['p', 'y', 't', 'h', 'o', 'n']

for a in lst :
    print(a * 2)

print('========')
length = len(lst)
for i in range(length) :
    print('Value at ', i, ' or ', i - length, ' is - ', lst[i])

print('========')    
length = len(lst)
for i in range(length - 1) :
    print(lst[i], lst[i + 1])
    
print('========')    
length = len(lst)
rev = -1
for i in range(length) :
    print(lst[i], lst[rev])
    rev-=1
