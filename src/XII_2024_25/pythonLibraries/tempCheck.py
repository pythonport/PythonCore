'''
Created on Jul 18, 2024

@author: admin
'''
import tempConversion as tc

print(tc.freezing_f)
print(tc.freezing_c)

temp_c = -40
temp_f = tc.to_fahrenheite(temp_c)
print(temp_c, '.c =', temp_f,'.f')