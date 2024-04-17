'''
Created on Aug 22, 2023

@author: Admin
'''
import pickle
fh = open('aboutBinary.info','rb')
try :
    st1 = pickle.load(fh)
    lstr1 = st1.split()
    print(lstr1)
    print('String is - ',lstr1[0])
except :
    fh.close()