'''
Created on Dec 22, 2025

@author: admin
'''
marks = int(input('Enter marks - '))
if marks > 80:
    print('Grade - A+')
elif marks > 60:
    print('Grade - A')
elif marks > 50:
    print('Grade - B')
elif marks > 33:
    print('Grade - C')
else :
    print('Grade - D')
