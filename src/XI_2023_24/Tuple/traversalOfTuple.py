'''
Created on Jan 10, 2024

@author: Admin
'''
vowels = ('a','e','i','o','u')
print(vowels)

for value in vowels :
    print(value, end=' ')

print()  
for a in range(len(vowels)) :
    print(vowels[a])
    
tpython = tuple('python')

for a in tpython:
    print(a)