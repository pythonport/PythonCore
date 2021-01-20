'''
Created on Sep 9, 2020
Stack implementation using list (passing list as item) in python
@author: Rajesh Kuamr Jha, PGT(Computer Science)
'''

###### STACK IMPLEMENTATION ##############


def isEmpty(stk):
    if stk == [] :
        return True
    else :
        return False


def push(stk, item):
    stk.append(item)
    top = len(stk) - 1


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


def display(stk):
    if isEmpty(stk):
        return 'Stack is Empty'
    else :
        top = len(stk) - 1
        print(stk[top], ' <- top')
        for a in range(top - 1, -1, -1):
            print(stk[a])


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
        mlst=[]
        mno = int(input("Member Number - "))
        mname = input("Member Name - ")
        mage = int(input("Member Age - "))
        mlst.append(mno)
        mlst.append(mname)
        mlst.append(mage)
        push(stack, mlst)
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
