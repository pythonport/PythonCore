'''
Created on Jul 11, 2019

@author: admin
Arithmatic progression
Program to generates a series using a function which takes first and last 
value of the series and then generate four terms that are equidistant.eg
if 1 and 7 the output should 1 3 5 7
'''


def genEquFourNum(st, en):
    d = (en - st) / 3
    s = [st, st + d, st + 2 * d, st + 3 * d]
    return s

st = int(input('Enter first number - '))
en = int(input('Enter second number - '))

equLst = genEquFourNum(st,en)
print ('Four equal numbers are - ',equLst)