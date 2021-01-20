'''
Created on Aug 17, 2019
Example of list Comprehension
@author: admin
'''
lst = []
for i in range(10):
    lst.append(i ** 2)

print(lst)
print('-' * 40)

lst1 = [i ** 2 for i in range(10)]

print(lst1)
print('-' * 40)
lst3 = []
for i in range(1, 50):
    if i % 7 == 0:
        lst3.append(i)
        
print(lst3)
print('-' * 40)

lst4 = [i for i in range(1, 50) if i % 7 == 0]
print(lst4)
print('-' * 40)

num = int(input("Enter number to get table of that - "))
lst5 = [i*num for i in range(1,11)]
print(lst5)