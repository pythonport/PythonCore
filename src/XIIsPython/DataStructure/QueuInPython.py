'''
Created on Oct 14, 2019

Queue Implementation in Python as a list
front : integer having position of first(frontmost) element in stack
rear : integer having position of last element in stack

@author: admin
'''


def isEmpty(qu):
    if qu == []:
        return True
    else:
        return False


def enqueue(qu, item):
    qu.append(item)
    if len(qu)==1:
        front=rear=0
    else:
        rear = len(qu) - 1


def dequeue(qu):
    if isEmpty(qu):
        return "UnderFlow"
    else:
        item = qu.pop(0)
    if len(qu) == 0:
        front=rear=0
    return item

    
def peek(qu):
    if isEmpty(qu):
        return "UnderFlow"
    else:
        front=0
        return qu[front]


def display(qu):
    if isEmpty(qu):
        return "Queue Is Empty"
    else :
        front = 0
        rear = len(qu)-1
        print(qu[front], '<-front')
        for a in range(1,rear):
            print(qu[a])
        print(qu[rear],'<-rear')
        
#---Main-----
highestpr = []
normalpr = []
lowerstpr = []
front = None
while True:
    print('*' * 20)
    print('Queue OPERATIONS')
    print('1. Enqueue')
    print('2. Dequeue')
    print('3. Peek')
    print('4. Display queue')
    print('5. Exit')
    ch = int(input('Enter your choice(1-5) :'))
    print('-' * 20)
    if ch == 1:
        element = int(input('Enter element : '))
        priority = input('Higher/Normal/Lower - [h/n/l] -')
        if priority=='h':
            enqueue(highestpr, element)
        if priority=='n':
            enqueue(normalpr, element)
        if priority=='l':
            enqueue(lowerstpr, element)
        
        input('Press Enter to continue...')
    elif ch == 2:
        priority = input('Higher/Normal/Lower - [h/n/l] -')
        element = None
        if priority=='h':
            element=dequeue(highestpr)
        if priority=='n':
            element=dequeue(normalpr)
        if priority=='l':
            element=dequeue(lowerstpr)
            
        if element == "UnderFlow" :
            print("UNDERFLOW! Queue is empty")
        else :
            print("De-queue-ed item is ", element)
        input('Press Enter to continue...')
    elif ch == 3:
        priority = input('Higher/Normal/Lower - [h/n/l] -')
        element = None
        if priority=='h':
            element=peek(highestpr)
        if priority=='n':
            element=peek(normalpr)
        if priority=='l':
            element=peek(lowerstpr)
            
        if element == 'UnderFlow':
            print('Queue is empty')
        else:
            print('Front element is : ', element)
        input('Press Enter to continue...')
    elif ch == 4:
        priority = input('Higher/Normal/Lower - [h/n/l] -')
        element = None
        if priority=='h':
            element=display(highestpr)
        if priority=='n':
            element=display(normalpr)
        if priority=='l':
            element=display(lowerstpr)
        input('Press Enter to continue...')
    elif ch == 5:
        break
    else:
        print("Invalid choice")
        input('Press Enter to continue...')
