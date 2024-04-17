'''
Created on Feb 16, 2022
Write a program that displays options for inserting or 
deleting elements in a list. If the user choose a deleting option
display a submenu and ask if element is to be deleted with value
or by using its position of a list slice is to be deleted.
@author: admin
'''

val = [17, 23, 18, 19]
print('The list is : - ', val)
while True :
    print('Main Menu')
    print('1. Insert')
    print('2. Delete')
    print('3. Exit')
    ch = int(input('Enter choice 1/2/3 - '))
    if ch == 1 :
        item = int(input('Enter item :- '))
        pos = int(input('Insert at which position - '))
        index = pos - 1
        val.insert(index, item)
        print('Success! Lis is now : - ', val)
    elif ch == 2 :
        pass
    elif ch == 3 :
        print("Exiting...")
        break;
    else :
        print("valid choices are 1/2/3")
