'''
Created on Jan 18, 2021
Program to demonstrate the difference between
break and continue
@author: admin
'''
print('The loop with "Break" produces output as : ')
for i in range(1, 11):
    if i % 3 == 0:
        break
    else:
        print(i)
        
print('The loop with "Continue" produces output as : ')
for i in range(1, 11):
    if i % 3 == 0:
        continue
    else:
        print(i)   
