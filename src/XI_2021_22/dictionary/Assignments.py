'''
Created on Mar 15, 2022

@author: admin
'''
d = {1:'mon', 2:'tue', 3:'wed', 4:'thu', 5:'fri', 6:'sat', 7:'sun'}
print('length of dictonary - ', len(d))
print('4th day - ', d[4])
print('Last value removed - ', d.pop(7))
print('Last key value removed - ', d.popitem())
d.clear()
print('Dictionary after deleting all element - ', d)
print('Deleting dictionary itself')
del d
print('OK')
