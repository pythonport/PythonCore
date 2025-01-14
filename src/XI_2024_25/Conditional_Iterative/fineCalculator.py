'''
Created on Dec 28, 2024

@author: admin
'''
bookIssued = int(input('Enter no of books issued - '))
days = int(input('For no of days - '))
fine = 0
if days > 15 :
    fine = bookIssued * 10
elif days > 10 :
    fine = bookIssued * 7
elif days > 5 :
    fine = bookIssued * 3
else :
    print('No fine imposed')

print('For {} books for {} days fine amount is {}'.format(bookIssued, days, fine))    