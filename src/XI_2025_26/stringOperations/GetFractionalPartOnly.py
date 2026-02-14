'''
Created on Feb 9, 2026

@author: admin
'''
num = input('Float to get decimal part only - ')
numtpl = num.partition('.')
print('Integer part is - ',numtpl[0])
print('Decimal part is - ',numtpl[2])