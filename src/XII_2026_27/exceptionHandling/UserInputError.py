'''
Created on Jul 27, 2026
Code to demonstrate the use of try and except block in user input
@author: admin
'''
ok = False
while not ok :
    try :
        strnum = input('Enter integer number - ')
        num = int(strnum)
        ok = True
    except :
        print('Enter INTEGER ONLY')

print('Correct integer is - ',num)