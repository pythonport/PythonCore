'''
Created on Aug 29, 2026

@author: admin
'''
import pickle
fout = open('studentdata.dat','wb')
stu = {}
ans = 'y'
while ans =='y':
    roll = input('Roll - ')
    name = input('name - ')
    marks = int(input('marks - '))
    stu['roll']=roll
    stu['name']=name
    stu['marks']=marks
    pickle.dump(stu,fout)
    
    ans = input('Do you want more record [y/n] - ')

print('done')
fout.close()