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
queue = []
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
        item = int(input('Enter item : '))
        enqueue(queue, item)
        input('Press Enter to continue...')
    elif ch == 2:
        item = dequeue(queue)
        if item == "UnderFlow" :
            print("UNDERFLOW! Queue is empty")
        else :
            print("De-queue-ed item is ", item)
        input('Press Enter to continue...')
    elif ch == 3:
        item = peek(queue)
        if item == 'UnderFlow':
            print('Queue is empty')
        else:
            print('Front element is : ', item)
        input('Press Enter to continue...')
    elif ch == 4:
        display(queue)
        input('Press Enter to continue...')
    elif ch == 5:
        break
    else:
        print("Invalid choice")
        input('Press Enter to continue...')
