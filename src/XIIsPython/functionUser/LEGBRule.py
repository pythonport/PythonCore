'''
Created on Apr 18, 2019

@author: admin
'''
def state1():
    global tigers
    tigers = tigers-15
    print('2- ',tigers)

tigers = 95
print('1- ',tigers)
print('11- ',tigers)
state1()
print('3- ',tigers)
state1()
print('4- ',tigers)