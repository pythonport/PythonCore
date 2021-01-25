'''
Created on Jan 21, 2021
prime number between range of number
@author: admin
'''

for num in range(10, 50):
    lim = int(num / 2) + 1
    for a in range(2, lim) :
        rem = num % a
        if rem == 0 :
            print(num, " is not a Prime Number  is divisible by ", a)
            break
    else :
        print(num, " is a prime number")
