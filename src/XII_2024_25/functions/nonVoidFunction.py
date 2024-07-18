'''
Created on Apr 18, 2024

@author: admin
'''
#non-void function
def calcsum(a, b):
    return a + b

a = calcsum(100,150)
print(a)

print(calcsum(100,200))

doublea = calcsum(100,150)*2
print(doublea)

calcsum(80,40)

print('======void with return =========')
def calc(x, y=5, c=10):
    val = x*y
    print(val , 'inside function')
    return

a = calc(10,12)
print(a)
print(calc(100))

