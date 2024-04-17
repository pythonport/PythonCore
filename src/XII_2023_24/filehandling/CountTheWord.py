'''
Created on Aug 30, 2023

@author: Admin
'''
fh = open('poem.txt', 'r')
str = fh.read()
lstr = str.split()
count_the = 0
count_to = 0
for a in lstr:
    if a == 'the':
        count_the += 1
    if a == 'get':
        count_to += 1

print('Total no of the is - ', count_the)
print('Total no of the is - ', count_to)
