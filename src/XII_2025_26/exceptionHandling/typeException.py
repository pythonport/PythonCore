'''
Created on Sep 2, 2025
Program ensure an valid integer has been passed by user.
@author: admin
'''
flag = False
while not flag :
    try :
        a = input('Enter number - ')
        inta = int(a)
        flag = True
    except :
        print('Invalid input convert into integer')
    
print('done')