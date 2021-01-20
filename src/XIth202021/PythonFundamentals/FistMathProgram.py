'''
Created on Sep 7, 2020
@author: admin
'''
stack = [67, 55, 44, 33, 44, 67]

peek = stack[len(stack)-1]
print("Pick of stack is - ",peek)

a = stack.pop()     #pop operation of stack
print('Popped data is - ',a)

peek = stack[len(stack)-1]
print("Pick of stack is - ",peek)

b = stack.pop(3)    #pop operation of stack
print('Popped data is - ',b)

print(stack)
stack.append(66)  #push operation of stack
stack.append(78)
print(stack)
