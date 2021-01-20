'''
Created on Oct 11, 2019

Stack Implementation in Python as a list
top : integer having position of topmpost element in stack

@author: admin
'''


def isEmpty(stk):
    if stk == []:
        return True
    else:
        return False


def push(stk, item):
    stk.append(item)
    top = len(stk) - 1


def pop(stk):
    if isEmpty(stk):
        return "UnderFlow"
    else:
        item = stk.pop()
        if len(stk) == 0:
            top = None
        else :
            top = len(stk) - 1
        return item

    
def peek(stk):
    if isEmpty(stk):
        return "UnderFlow"
    else:
        top = len(stk) - 1
        return stk[top]


def display(stk):
    if isEmpty(stk):
        return "UnderFlow"
    else :
        top = len(stk) - 1
        print(stk[top], '<=top')
        for a in range(top - 1, -1, -1):
            print(stk[a])


#---Main-----
stack = []
top = None
while True:
    print('*'*20)
    print('STACK OPERATIONS')
    print('1. Push')
    print('2. Pop')
    print('3. Peek')
    print('4. Display stack')
    print('5. Exit')
    ch = int(input('Enter your choice(1-5) :'))
    print('-'*20)
    if ch == 1:
        #item = int(input('Enter item : '))
        item = []
        bid = input("Enter book ISBN No : ")
        bname = input("Enter book name : ")
        price = input("Enter book price : ")
        item.append(bid)
        item.append(bname)
        item.append(price)
        push(stack, item)
    elif ch == 2:
        item = pop(stack)
        if item == "UnderFlow" :
            print("UNDERFLOW! Stack is empty")
        else :
            print("Popped item is ", item)
    elif ch == 3:
        item = peek(stack)
        if item == 'UnderFlow':
            print('Underflow! Stack is empty')
        else:
            print('Topmost element is : ', item)
    elif ch == 4:
        display(stack)
    elif ch == 5:
        break
    else:
        print("Invalid choice")