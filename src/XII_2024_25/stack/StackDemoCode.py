'''
Created on Oct 12, 2024

@author: admin
'''
def isEmpty(stk):
    if stk == [] :
        return True
    else :
        return False
    
def push(stk, item):
    stk.append(item)
    top = len(stk) - 1
    
def display(stk):
    if isEmpty(stk):
        print('Stack is Empty')
    else :
        top = len(stk) - 1
        print('|'+str(stk[top])+'|'+ ' <- top')
        for a in range(top - 1, -1, -1):
            print('|'+str(stk[a])+'|')
        print('___')    
            
def pop(stk):
    if isEmpty(stk) :
        return 'Underflow'
    else :
        item = stk.pop()
        if len(stk) == 0 :
            top = None
        else :
            top = len(stk) - 1
        return item
    
def peek(stk):
    if isEmpty(stk):
        return 'Underflow'
    else :
        top = len(stk) - 1
        return stk[top]

    
# MAIN
stack = []
top = None
while True :
    print('******************')
    print('STACK OPERATIONS')
    print('1. Push')
    print('2. Pop')
    print('3. Peek')
    print('4. Display Stack')
    print('5. Exit')
    print('******************')
    ch = int(input('Enter your choice [1-5]- '))
    if ch == 1 :
        item = int(input("Enter item to be inserted in stack - "))
        push(stack, item)
    elif ch == 2 :
        item = pop(stack)
        if item == 'underflow' :
            print('Underflow ! Stack is empty')
        else :
            print("Popped item is  - ", item)
    elif ch == 3 :
        item = peek(stack)
        if item == 'underflow' :
            print('Underflow ! Stack is empty')
        else :
            print("Topmost item is  - ", item)
    elif ch == 4 :
        display(stack)    
    elif ch == 5 :
        print("*** Thank you ***")
        break    
    else :
        print("Invalid input Try again !")