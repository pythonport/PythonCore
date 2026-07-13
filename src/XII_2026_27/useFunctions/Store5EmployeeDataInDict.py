'''
Created on Apr 15, 2026

@author: admin
'''
employees = {}
for i in range(5):
    ename = input('Employee name - ')
    salary = int(input('Salary - '))
    employees[ename]=salary

print('Employee list')
for key,value in employees.items():
    print(f'{key}->{value}')
    #print(key,'->',value)