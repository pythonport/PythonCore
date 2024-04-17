'''
Created on Aug 22, 2023

@author: Admin
'''
import pickle

fh = open('aboutBinary.info','wb')
str = 'This program is going to store string data into the binary file and in binary format only.'
pickle.dump(str, fh)
print('done')