'''
Created on Aug 25, 2025

@author: admin
'''
import pickle
fh = open('stufee.dat','rb+')
flag = False
sid = int(input('Enter student code - '))
marks = float(input('New Marks - '))
try :
    while True :
        stu ={}
        rpos = fh.tell()
        stu = pickle.load(fh)
        if stu['rollno'] == sid :
            stu['marks'] = marks
            fh.seek(rpos)
            pickle.dump(stu, fh)
            flag = True
            
except EOFError :
    if flag == False :
        print('No record found')
    else :
        print('updation done')
    fh.close()