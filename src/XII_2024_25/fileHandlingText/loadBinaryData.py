'''
Created on Sep 10, 2024
Reading the data from the binary file
@author: admin
'''
import pickle
fout = open('stulist.dat','rb')
stulist = pickle.load(fout)
for i in stulist :
    print(i)