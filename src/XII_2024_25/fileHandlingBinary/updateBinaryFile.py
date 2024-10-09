'''
Created on Sep 13, 2024

@author: admin
'''
import pickle
stufile = open('studentdata.dat', 'rb')
try:
    while True :
        student = pickle.load(stufile)
        if student['roll']=='' :
            print('record found')
            print(student)
            student['roll'] = 5
            print(student)
            
except EOFError:
    print('done')
    stufile.close()