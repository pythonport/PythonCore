'''
Created on Sep 6, 2025

@author: admin
'''
try :
    fh = open('exception.txt')  #Write file name which doesnot exist
    print(fh.read())
    v = 10/10  # v = 10/0
    a = int(88.5)  # a = int('ab')
    lst = [2,3,4]
    print(lst[2]) # print(lst[6])
    radius = None # Name error as radius not defined
except IOError as e :
    print("File not found - ", e)
except ZeroDivisionError :
    print('Alert! - Zero Division Exception')
except ValueError :
    print('Alert! - Cant convert into int')
except IndexError :
    print('Alert! - Index out of range')
except :
    print('System is down, wait for some time')  
else :
    print('I am happy, no error in code')