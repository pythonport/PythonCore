'''
Created on Feb 25, 2022
input a tuple and check if it contains all the elements as same.
@author: admin
'''

t = eval(input('Enter tuple of same element - '))
len = len(t)
count = t.count(t[0])

if len==count :
    print("Tuple having same element in every position")
else :
    print("Tuple NOT having same element in every position")
    
print("Thank you")