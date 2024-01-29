'''
Created on Jan 10, 2024

@author: Admin
'''

def calc(**args):
    for key, value in args.items() :
        print('{} => {}'.format(key,value))
        
calc(name = 'rajesh', clas='11', section='A', fee=500)


def calc(*args):
    for value in args :
        print(value)
        
calc('rajesh', '11', 'A')