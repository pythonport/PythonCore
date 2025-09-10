'''
Created on Aug 20, 2025

@author: admin
'''
import pickle
fh = open('feelist.dat','rb')
try :
    while True :
        student = pickle.load(fh)
        if student[2] > 50 :
            print('Roll - ',student[0])
            print('Name - ',student[1])
            print('Fee - ',student[2])
except :
    fh.close()