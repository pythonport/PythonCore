'''
Created on Aug 6, 2022

@author: admin
'''
import tempConversion as tc

temp = float(input("Enter temp in centi - "))

tempf = tc.to_fahrenheite(temp)
print("Temp in centi - ", temp)
print("Temp in feh - ", tempf)

print("Freezing in Feh - ", tc.freezing_f)
print("Freezing in cent - ", tc.freezing_c)
