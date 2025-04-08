'''
Created on Feb 19, 2025

@author: admin
'''
dict = {'Mohan':95,'Ram':89,'Suhel':92,'Sangeeta':85}
print(dict['Sangeeta'])
dict['Sangeeta'] = 99  #updating the existing key value
print(dict['Sangeeta'])
print(dict)
dict['meena']=78  #adding the new key value
print(dict)

print('meena' in dict)