'''
Created on Mar 11, 2022

@author: admin
'''
stu1 = {1:'Neha',2:[2,3,5,6],3:'Avnit',4:'Ana'}
stu2 = stu1.copy()
stu1[1]='Megha'
print('stu1 - ',stu1)
print('stu2 - ',stu2)

print('----------')
stu1[2].append(8)
print('stu1 - ',stu1)
print('stu2 - ',stu2)