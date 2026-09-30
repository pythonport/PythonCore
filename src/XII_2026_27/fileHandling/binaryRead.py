'''
Created on Aug 27, 2026

@author: admin
'''
import pickle
fout = open('listData.dat','rb')
lst = pickle.load(fout)
print(lst)
fout.close()
print('done')