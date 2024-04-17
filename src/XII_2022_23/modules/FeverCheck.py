'''
Created on Sep 2, 2021
module to check fever in fahrenheite and centigrade
@author: admin
'''
from tempConversion import  *

tempf = float(input("Enter fever in fahrenheite - "))
tempc = to_centigrade(tempf)

print("fever in C is {0} and F is  {1}".format(tempc, tempf))
