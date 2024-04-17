'''
Created on Aug 22, 2023

@author: Admin
'''
import pickle

with open('employeedata.dat', 'rb') as fh:
    data = {}
    while True:
        data = pickle.load(fh)
        print(data)
