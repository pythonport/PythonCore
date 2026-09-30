'''
Created on Aug 29, 2026
Code to search record in binary file
@author: admin
'''
import pickle
fout = open('studentdata.dat','rb')
stu = {}
searchKey = ['2','3']
found = False
try :
    while True :
        stu = pickle.load(fout)
        #print(stu)
        if stu['roll'] in searchKey :
            print(stu)
            found = True
except EOFError :
    if found :
        print('Search completed')
    else :
        print('no record found')
    fout.close()
        
        