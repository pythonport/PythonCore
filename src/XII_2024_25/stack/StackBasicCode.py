'''
Created on Oct 13, 2024

@author: admin
'''

def push_data(stk, item):
    stk.append(item)

def pop_data(stk):
    item = stk.pop()
    return item

stk = []
push_data(stk, 12)
push_data(stk, 34)
push_data(stk, 22)
push_data(stk, 76)
top = len(stk)-1
print('stack after four push - ',stk)
print('stack pick is  - ',stk[top])

pop_data(stk)
pop_data(stk)
top = len(stk)-1
print('stack after two pop operation - ',stk)
print('stack pick is  - ',stk[top])