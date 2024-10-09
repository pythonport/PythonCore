'''
Created on Sep 12, 2024

@author: admin
'''
import pickle
stufile = open('studentdata.dat', 'rb')
try:
    while True :
        student = pickle.load(stufile)
        print(student)
except EOFError:
    print('done')
    stufile.close()

'''

import pickle
stufile = open('studentdata.dat', 'rb')
while True :
    student = pickle.load(stufile)
    print(student)

print('done')
stufile.close()
'''