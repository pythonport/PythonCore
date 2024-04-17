'''
Created on Dec 27, 2023

@author: Admin
'''
for i in range(7):
    for j in range(i):
        print('#', end=' ')
    print()
    
print('---------')
str = '# '
pattern = ''
for i in range(5) :
    pattern +=str
    print(pattern)