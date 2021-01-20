'''
Created on Jul 4, 2019
program to iterate list element
@author: admin
'''
lst = [3, 4, 5, 2, 3, 6]  # homoginous list

lstnew = ['one', 87, 76, 89.4, 334.54, 'two three', [4, 5, 3]]  #hegroginous list

print(lstnew)
print("========")

for i in lst:
    print(i)
print("========")   
 
for i in range(len(lstnew)):
    print(lstnew[i])
