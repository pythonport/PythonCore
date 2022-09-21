'''
Created on Jul 27, 2022

@author: admin
'''


def sum(a, b):  # a an b are parameters
    sum = a + b
    print("sum of {0} and {1} is {2}".format(a, b, sum))

'''
sum(34, 40)  # 34 an 40 are arguments
sum(23, 22)
m1 = 70
sum(m1, 50)
'''
sum(78, 45)  # positional or required
sum(a=89, b=78)  # keyword argument
sum(b=89, a=78)  # keyword argument

x, y = 90, 45
x = y = z = 100
sum(x, b = 90)  # positional or required
