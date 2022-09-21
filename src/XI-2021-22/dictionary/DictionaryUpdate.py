'''
Created on Mar 11, 2022

@author: admin
'''

emp1 = {"name":'abc', 'salary':56000,'location':'bokaro'}
emp2 = {"name":'xyz', 'salary':78000,'department':'sales'}
print(emp1)
print(emp2)
emp1.update(emp2)
print("------after update------")
print('emp1 -',emp1)
print('emp2 -',emp2)