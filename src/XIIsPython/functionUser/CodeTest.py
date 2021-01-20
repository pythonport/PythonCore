'''
Created on Apr 16, 2019

@author: admin
'''

"Jawahar navodaya vidyalaya".isdigit()
a = 23
print('Outside function ',a)

def valueOfA():
    b= "local b"
    a+2
    print('Inside function ',a+2)
    print(b)

valueOfA()
print('Outside function 2 - ',a)