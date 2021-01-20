'''
Created on Feb 28, 2019

@author: admin
'''
def hello():
    print('Hello function')
    def hi():
        print('Hi function')
        
    hi()

print(__name__)