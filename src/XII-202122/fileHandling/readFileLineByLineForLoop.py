'''
Created on Sep 17, 2021

@author: admin
'''
myfile = open('poem.txt', 'r')
str = ' '
counter = 0
while str :
    counter += 1
    str = myfile.readline()
    print(str)

print("Total number of lines are  - ", counter)
print('ok')
