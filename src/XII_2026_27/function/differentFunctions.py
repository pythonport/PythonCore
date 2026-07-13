'''
Created on Apr 21, 2026

@author: admin
'''
def sum(x,y):
    res = x+y
    a = 10/0
    return res

def greeting():
    print('inside function',__name__)
    print('GOOD MORNING')

print(__name__)
print(sum(10,20))
greeting()