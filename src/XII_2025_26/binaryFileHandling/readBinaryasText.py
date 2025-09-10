'''
Created on Aug 21, 2025

@author: admin
'''
import pickle
fh = open('feelist.dat','rb')
try :
    while True :
        st = pickle.load(fh)
        print(st)
except :
    fh.close()