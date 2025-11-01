'''
Created on Sep 10, 2025

@author: admin
'''
stk = []

def push_data(stk, item):
    stk.append(item)
    
def pop_data():
    if len(stk)==0 :
        return 'Underflow'
    else :
        item = stk.pop()
        return item

push_data(stk, 45)
push_data(stk, 12)
push_data(stk, 63)
push_data(stk, 44)

print('Stack is - ',stk)
print('Peak is - ',stk[-1])

element = pop_data()
print('popped data is - ',element)
element = pop_data()
print('popped data is - ',element)

print('Stack is - ',stk)
print('Peak is - ',stk[-1])

element = pop_data()
print('popped data is - ',element)
element = pop_data()
print('popped data is - ',element)
element = pop_data()
print('popped data is - ',element)