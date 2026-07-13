'''
Created on Apr 4, 2026
program to iterate tuple and list together and print the house attendance.
@author: admin
'''
houses = ('arawali', 'nilgiri', 'shivalik', 'udayagiri')
attendance = [38, 39, 41, 42]
count = 0
for house in houses:
    #print(f'Attendance of {house} is {attendance[count]}')
    print(f'{house} -> {attendance[count]}')
    count += 1
