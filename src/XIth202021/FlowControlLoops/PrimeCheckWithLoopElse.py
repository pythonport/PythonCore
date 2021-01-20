'''
Created on Jan 19, 2021
Prime Check with loop else
@author: admin
'''

num = int(input("Enter any number - "))
lim = int(num / 2) + 1
for a in range(2, lim) :
    rem = num % a
    if rem == 0 :
        print(num, " is not a Prime Number  is divisible by ", a)
        break
else :
    print(num, " is a prime number")
