'''
Created on Jan 24, 2025

@author: admin
'''
st = input('String without space - ')
total = 0
for i in st:
    if (i.isalpha() & i.islower()) :
        position = ord(i) - ord('a') + 1
        total += position
        print('Position of {} is - {}'.format(i, position))
print('sum of position - ', total)
