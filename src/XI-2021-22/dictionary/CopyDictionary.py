'''
Created on Mar 11, 2022

@author: admin
'''
stu1 = {1:'Neha',2:'Saima',3:'Avnit',4:'Ana'}
stu3 = stu1

print('Student 3 - ',stu3)
print('Student 1 - ',stu1)
print('=============')
stu1[2]='Sunita'
print('Student 3 - ',stu3)
print('Student 1 - ',stu1)
print('=============')
stu2 = stu1.copy()
stu1[2]='Amaita'
print('Student 3 - ',stu3)
print('Student 2 - ',stu2)
print('Student 1 - ',stu1)