'''
Created on Jul 12, 2024

@author: admin
'''
def function1(a):
    print('inside function')
    print('value received ',a)
    a+=2
    print('value changed ',a)
    print('returned form function')
    
num = 3
print('num before calling function ',num)
funcation1(a)
print('num before calling function ',num)
    