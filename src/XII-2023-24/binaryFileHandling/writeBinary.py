'''
Created on Aug 16, 2023

@author: Admin
'''

import pickle

fh = open('studentList.dat','wb')
lst = ['harish','girish','harsh','uday','vinay','prince',]

pickle.dump(lst, fh)
print("dumped successfully.")
fh.close()