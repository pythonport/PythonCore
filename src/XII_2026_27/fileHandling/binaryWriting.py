'''
Created on Aug 27, 2026

@author: admin
'''
import pickle

list = ['a','b','c','d','e']
fout = open('listData.dat','wb')
pickle.dump(list, fout)
fout.close()
print('done')