'''
Created on Apr 18, 2024

@author: admin
'''


def sendmessage(msg):
    print("Breaking news is - ")
    print(msg)

    
a = 'Today onward class will be till 01.00 PM only. \nYou can take rest after lunch'
sendmessage(a)


def calcsum(a, b):
    return a + b


summ = calcsum(10, 12)
print('sum is - ', summ)

a= calcsum(12, 3)
if (a > 10):
    print("value is more then 10 and value is - ",a)
