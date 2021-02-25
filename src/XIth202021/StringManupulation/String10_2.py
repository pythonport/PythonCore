'''
Created on Feb 1, 2021
Print string in forward and backward direction
@author: admin
'''

nm = input("Enter string to print - ")
length = len(nm)
i = 0
for a in range(-1, -length - 1, -1):
    print(nm[i] + "  " + nm[a])
    i += 1
