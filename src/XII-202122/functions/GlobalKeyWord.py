'''
Created on Aug 16, 2021

@author: admin
'''


def state1():
    global tigers
    tigers = 15
    print("local tiger - ",tigers)

    
tigers = float(95)
print("global tiger - ",tigers)
state1()
print("global tiger - ",tigers)
