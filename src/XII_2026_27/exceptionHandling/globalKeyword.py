'''
Created on Jul 31, 2026

@author: admin
'''
students = 45

def updateStuCount():
    global students
    students = 40
    print('Students in function - ',students)
    students+=20
    print('Students after update - ',students)

print('Students from global - ',students)    
updateStuCount()    
print('Students function call - ',students)    