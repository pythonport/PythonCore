'''
Created on Oct 1, 2026
Simple stack implementation code using push() and pop() function.
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

while True:
    ans = int(input('Push / Pop / display - [1,2,3] - ' ))
    if ans == 1 :
        item = int(input('Input item - '))
        push_data(stk, item)
    elif ans == 2:
        pval = pop_data()
        print('Popped item - ',pval)
    elif ans == 3:
        print(stk)
    else :
        print('EXITING ...')
        break     
'''
push_data(stk, 45)
push_data(stk, 12)
print('Stack is - ',stk)
print('Peak is - ',stk[-1])

element = pop_data()
print('popped data is - ',element)

print('Stack is - ',stk)
print('Peak is - ',stk[-1])
'''