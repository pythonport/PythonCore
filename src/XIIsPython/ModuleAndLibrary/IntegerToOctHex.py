'''
Created on Jul 11, 2019

@author: admin
'''
inum = int(input("Enter any numbet to get OCT and HeX - "))
bnum = bin(inum)
onum = oct(inum)
hnum = hex(inum)
print('Binary is %s Octal is %s and Hexa is %s of number %d ' % (bnum, onum, hnum, inum))
