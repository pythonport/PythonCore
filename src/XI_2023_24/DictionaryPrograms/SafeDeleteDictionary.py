'''
Created on Jan 27, 2024

@author: Admin
'''
emp = {1:50000, 2:525252, 3:65656, 4:524141}
print(emp)
key = int(input('Enter key - '))
if key  in emp:
    del emp[key]
    print(emp)
else:
    print('Key does not exists')
