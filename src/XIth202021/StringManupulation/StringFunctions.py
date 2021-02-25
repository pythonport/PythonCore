'''
Created on Feb 3, 2021

@author: admin
'''
s = "hello python"
print(s)
print(s.capitalize())

str1 = "hello parallel bbll"
substr = 'llw'
print("Value of count - ",str1.count(substr,5,13))

print('==============')
print("Value of find - ",str1.find(substr))

print('==============')
print("Value of index - ",str1.index(substr))