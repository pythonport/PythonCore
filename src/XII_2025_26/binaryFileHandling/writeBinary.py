'''
Created on Aug 6, 2025

@author: admin
'''
import pickle
fh = open('jnvdhanbad.dat','wb')
str = 'this is jnv dhanbad, class -12th science Computer Class'
lst = str.split()
print(lst)
pickle.dump(lst,fh)
fh.close()
print('done')