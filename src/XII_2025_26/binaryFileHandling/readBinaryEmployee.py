'''
Created on Aug 8, 2025
program to demonstrate the use of load function of pickle module with exception handling
@author: admin
'''
import pickle
fh = open('emp.dat','rb')
try :
    while True :
        nemp = pickle.load(fh)
        print(nemp)
except EOFError :
    print('file ended now ')
    fh.close()