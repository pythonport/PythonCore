'''
Created on Jul 8, 2019
Write a function that takes an number n and then return a randomly generated 
number having exactily n digits(not startig with zero) e.g, if n is 2 then 
function can randomly return a number 10-99 but 07,02 etc are ot valid ditit number.
@author: admin
'''
import random


def get_random(n):
    '''
    return - random number of n digit
    '''
    ub = 10 ** n - 1
    lb = 10 ** (n - 1)
    print("Upper is - ", ub)
    print("Lower is - ", lb)
    rnum = random.randint(lb, ub)
    return rnum


digitForRandom = int(input("Enter number of digit for random no [1,2,3,4 etc] - "))
rnum = get_random(digitForRandom)
print("Random number generated is - ", rnum)