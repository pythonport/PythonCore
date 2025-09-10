'''
Created on Aug 6, 2025

@author: admin
'''
import pickle
fh = open('jnvdhanbad.dat','rb')
lst = pickle.load(fh)
print(lst)