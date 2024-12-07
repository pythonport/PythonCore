'''
Created on Oct 13, 2024

@author: admin
'''
def push(L, Stk):
    for i in L:
        if i[0] == 'B' :
            Stk.append(i)

def display(stk):
    if stk==[] :
        print("stack is empty")
    else :
        print(stk)
        #for i in stk :
        #    print(i)

L = ['Bombay','Bangalore','chennai','delhi','Bokaro']
#L=[]
Stk = []
push(L, Stk)
display(Stk)