'''
Created on Sep 2, 2020
For loop for creating list
@author: admin
'''

lst = []
for num in range(1, 50):
    if num % 7 == 0 :
        lst.append(num)
    
print("List is - ", lst)

lst = [num for num in range(1, 50) if num % 7 == 0]
print("List is - ", lst)

lst = [num if num<5 else num*2 for num in range(2,9)]
lst = [(num if num<5 else num*2) for num in range(2,9)]
print("list is - ",lst)

lst = []
for num in range(2,9) :
    if num<5 :
        lst.append(num)
    else :
        lst.append(num*2)
print("list is - ",lst)

lst = [num if num % 7 == 0 else num//2for num in range(1, 50)]
print("List is - ", lst)