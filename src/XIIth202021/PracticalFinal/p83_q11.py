'''
Created on Jan 16, 2021
Write a method in python to display the elements of list thrice if it is
a number and display the element terminated with '#' if it is not a
number.
@author: admin
'''

lst = ['41', 'DROND', 'GIRIRAJ', '13', 'ZARA']
for a in lst :
    if a.isdigit()==True :
        print(a*3)
    else :
        print(a,'#')
