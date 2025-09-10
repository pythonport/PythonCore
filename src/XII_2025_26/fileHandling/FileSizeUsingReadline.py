'''
Created on Jul 29, 2025
Display the size of file after removing EOL chatacters, leading and trailing space and blank line
@author: admin
'''

fout = open('jangalbook.txt', 'r')
str = ' '
size = 0  # file size after removing space
tsize = 0  # total file size
while str:
    str = fout.readline()
    tsize = tsize + len(str)
    size = size + len(str.strip())
    print('Total - ', tsize, 'stripped - ', size)
print('Total file size = ', tsize)
print('File size after removing space = ', size)
