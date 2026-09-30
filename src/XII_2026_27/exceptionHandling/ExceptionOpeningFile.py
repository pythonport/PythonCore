'''
Created on Jul 27, 2026
Program to use finally block which runs always.
@author: admin
'''
try :
    fout = open('student.txt')
    stu = fout.read()
    print(stu)
except:
    print('No such file found')
finally:
    print('I am here always with you.')