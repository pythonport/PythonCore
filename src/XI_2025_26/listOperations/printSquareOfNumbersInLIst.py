'''
Created on Feb 13, 2026

@author: admin
'''
num = [2,4,6,8,10]

# first method
for a in num:
    print(a**2)
    
# second method
for a in range(len(num)):
    print(num[a]**2,'is the square of',num[a])