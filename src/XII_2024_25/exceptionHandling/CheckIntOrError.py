'''
Created on Oct 9, 2024

@author: admin
'''
ok = False
while not ok :
    try :
        a = input('Enter integer value - ')
        inta = int(a)
        ok = True
        print('Int value is - ',inta)
    except :
        print('Not a valid integer!')