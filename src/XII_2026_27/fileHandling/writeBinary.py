'''
Created on Jul 31, 2026

@author: admin
'''
import pickle
fout = open('studentList.dat','rb')
lst = pickle.load(fout)
print(lst)
print('done')