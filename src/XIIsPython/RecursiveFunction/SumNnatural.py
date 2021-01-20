'''
Created on Jul 26, 2019

@author: admin
'''


def sumNnum(num):
    if num == 1:
        return 1
    else :
        sum = num + sumNnum(num - 1)
        print("sum of %d is - %d" % (num, sum))
        return sum
    

num = int(input('Enter number to calculate sum of nums - '))

sum = sumNnum(num)
print('Sum of %d natural number is - %d' % (num, sum))