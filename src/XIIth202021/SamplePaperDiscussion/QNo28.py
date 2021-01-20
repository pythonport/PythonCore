'''
Created on Dec 17, 2020
Correct the code given
@author: admin
'''

Value = 30
for VAL in range(0, Value):     # Error 1
    if VAL % 4 == 0:            # Error 2
        print(VAL * 4)
    elif VAL % 5 == 0:          # Error 3
        print(VAL + 3)
    else:                       # Error 4
        print(VAL + 10)
