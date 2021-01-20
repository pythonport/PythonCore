'''
Created on Jan 18, 2021
Write a function that takes a number n  and then
returns a randomly generated number having exactly
n digits (not starting with zero). eg if n is 2 then 
function can randomly return a number 10-99 but 07,02
etc are not valid two digit numbers.
@author: admin
'''
import random
digit = int(input("Enter digit to get random number - "))
ub = 10 ** digit - 1
lb = 10 ** (digit - 1)

print("Lower bond - ", lb)
print("Upper bond - ", ub)

rnum = random.randint(lb, ub)

print("Random number between %d and %d is - %d" % (lb, ub, rnum))
#print("Random number between", lb, " and ", ub, " is - ", rnum)