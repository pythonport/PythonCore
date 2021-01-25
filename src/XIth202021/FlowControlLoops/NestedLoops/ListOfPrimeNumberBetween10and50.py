'''
Created on Jan 21, 2021
List all the prime numbers between
10 to 50
@author: admin
'''

lst = []
for num in range(10, 51):
    lim = int(num / 2) + 1
    for a in range(2, lim) :
        rem = num % a
        if rem == 0 :
            break
    else :
        lst.append(num)

print("List of all prime number between 10-50 is - \n",lst)