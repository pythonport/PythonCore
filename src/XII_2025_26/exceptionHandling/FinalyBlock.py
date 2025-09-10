'''
Created on Sep 6, 2025

@author: admin
'''
try :
    print(10/5)
except ZeroDivisionError as e :
    print(e)
finally:
    print('done')
    
''' finally without except block
try :
    print(10/5)
finally:
    print('done')
    
'''