'''
Created on Dec 31, 2020
Find output
@author: admin
'''
m1 = 'WeLcOME'
m2 = 'GUeSTs'
m3 = ''

for i in range(0, len(m2) + 1) :
    if m1[i] >= 'A' and m1[i] <= 'M':
        m3 = m3 + m1[i]
    elif m1[i] >= 'N' and m1[i] <= 'Z':
        m3 = m3 + m2[i]
    else :
        m3 = m3 + '*'

print(m3)        