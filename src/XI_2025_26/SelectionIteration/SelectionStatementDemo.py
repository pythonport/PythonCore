'''
Created on Dec 3, 2025
Selection statement demo program
@author: admin
'''
num = int(input('Enter number - '))

if num % 2 == 0:
    print(num, 'is Even')
else :
    print(num, 'is Odd')
    
print('OK')

# Iterative Statement demo code
sum = 0
for i in range(2, 51, 2) :
    sum  = sum+i

print('Sum of even number from 2-50 is - ',sum)