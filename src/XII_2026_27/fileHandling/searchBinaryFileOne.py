'''
Created on Aug 29, 2026

@author: admin
'''
import pickle
fout = open('studentdata.dat','rb')
stu = {}
try :
    while True :
        stu = pickle.load(fout)
        if int(stu['marks']) > 65 :
            print(stu)
            found = True
except EOFError :
    if found :
        print('Search completed')
    else :
        print('no record found')
    fout.close()