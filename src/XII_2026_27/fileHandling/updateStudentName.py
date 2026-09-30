'''
Created on Sep 10, 2026

@author: admin
'''
import pickle
fout = open('studentdata.dat','rb+')
stu = {}
found = False
try :
    while True :
        rpos = fout.tell()
        stu = pickle.load(fout)
        if stu['roll'] == str(4) :
            stu['name'] = 'Kamlesh'
            fout.seek(rpos)
            pickle.dump(stu, fout)
            found = True
except EOFError :
    if found :
        print('update completed')
    else :
        print('no record found')
    fout.close()