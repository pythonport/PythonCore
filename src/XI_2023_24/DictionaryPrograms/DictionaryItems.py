'''
Created on Jan 29, 2024

@author: Admin
'''
emp = {'name': 'rohan', 'salary': 505555, 'location': 'bangalore', 'dept': 'sales'}

elist = emp.items()
print(elist)
for items in elist :
    print(items)
    
print('-------')

for k, v in elist :
    print(k, ' =>', v)