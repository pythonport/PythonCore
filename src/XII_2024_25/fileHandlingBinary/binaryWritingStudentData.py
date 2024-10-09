'''
Created on Sep 12, 2024
Writing the data to binary file
@author: admin
'''
import pickle
stu = {}
stufile = open('studentdata.dat','ab')
ans = 'y'
while ans=='y':
    rno = input('roll no - ')
    name = input('name - ')
    marks = input('marks - ')
    stu['roll'] = rno
    stu['name'] = name
    stu['marks'] = marks
    pickle.dump(stu, stufile)
    ans = input('do you want to continue [y/n]- ')

stufile.close()