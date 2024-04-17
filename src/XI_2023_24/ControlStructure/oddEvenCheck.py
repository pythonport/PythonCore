'''
Created on Dec 2, 2023

@author: Admin
'''
num = int(input('Number - '))

if num%2==0 :
    print(num,' is even number')
else :
    #print(num,' is odd number')
    print('{0} is odd number'.format(num))