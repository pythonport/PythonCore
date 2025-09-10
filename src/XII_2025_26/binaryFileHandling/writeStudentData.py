'''
Created on Aug 20, 2025

@author: admin
'''
import pickle
fh = open('feelist.dat','ab')

for i in range(3):
    student = []
    roll = int(input('roll - '))
    name = input('Name - ')
    fee = float(input('Fee - '))
    
    student.append(roll)
    student.append(name)
    student.append(fee)
    
    pickle.dump(student, fh)

fh.close()
print('writing done')