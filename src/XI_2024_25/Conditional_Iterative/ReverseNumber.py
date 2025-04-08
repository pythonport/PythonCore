'''
Created on Jan 17, 2025
to reverse the number in place
@author: admin
'''
num = int(input('Enter number to reverse - '))

onum = num
reverse = 0
for i in range(len(str(onum))):
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
    #print(reverse)
    
    
print('original number - ', onum)
print('reverse number - ', reverse)
