'''
Created on Sep 7, 2026

@author: admin
'''
import pickle
fout = open('studentdata.dat','rb+')
stu = {}
try :
    while True :
        rpos = fout.tell()
        stu = pickle.load(fout)
        if int(stu['marks']) > 80 :
            stu['marks'] = stu['marks'] + 2
            fout.seek(rpos)
            pickle.dump(stu, fout)
            found = True
except EOFError :
    if found :
        print('update completed')
    else :
        print('no record found')
    fout.close()