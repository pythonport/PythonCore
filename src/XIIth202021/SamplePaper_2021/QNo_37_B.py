'''
Created on Jan 5, 2021
Write a function in Python PUSH(Arr), 
where Arr is a list of numbers. 
From this list push all numbers divisible by 5 
into a stack implemented by using a list. 
Display the stack if it has at least one element, 
otherwise display appropriate error message.
QNo-37_A Sample Paper
@author: admin
'''
def PUSH(arr):
    stack = []
    for i in arr:
        if i % 5 == 0:
            stack.append(i)
    if len(stack) == 0:
        print("Error : Empty stack")
    else :
        print('Stack is - ', stack)
        
#array = [34, 55, 66, 25, 15, 78]
array = [34, 51, 66, 26, 19, 78]
PUSH(array)
