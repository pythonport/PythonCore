'''
Created on Jan 5, 2021
Write a function in Python POP(Arr), 
where Arr is a stack implemented by a 
list of numbers. The function returns 
the value deleted from the stack.
QNO - 37_B of Sample Paper
@author: admin
'''


def POP(arr):
    if len(arr) == 0 :
        print("Error: Underflow")
    else :
        a = arr.pop()
        return a


# array = [34, 51, 66, 26, 19, 78]
array = []
poppedVal = POP(array)
print("Popped value is  - ", poppedVal)
