'''
Created on Feb 19, 2025

@author: admin
'''

#traversal in dictionary
dict = {'Mohan':95,'Ram':89,'Suhel':92,'Sangeeta':85}
for key in dict :
    print(key,' - ',dict[key])
    
    
#------------
for key,value in dict.items() :
    print(key,' - ',value)