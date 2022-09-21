'''
Created on Jul 30, 2022

@author: admin
'''


def red():
    a = 89

    def blue():
        b = 67
        print('line - 13 - ',a)
        print('line - 14 - ',b)
    
    blue()
    print('line - 17 - ',a)


red()  # at global level