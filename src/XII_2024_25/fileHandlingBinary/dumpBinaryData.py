'''
Created on Sep 10, 2024
Writing the data to the binary file
@author: admin
'''
import pickle
fout = open('stulist.dat','wb')
stulist = [['Alok','90','first'],['Ankita','95','first'],['Binit','55','second']]
pickle.dump(stulist, fout)
print('done')


#loadBinaryData
import pickle
fout = open('stulist.dat','rb')
stulist = pickle.load(fout)
for i in stulist :
    print(i)