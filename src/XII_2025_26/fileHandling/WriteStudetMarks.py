'''
Created on Jul 30, 2025

@author: admin
'''
file = open('stumarks.dat','w')
count = int(input('Number of students - '))
for i in range(count) :
    print(i+1, ': Student Record')
    roll = input('Roll no - ')
    name = input('Name - ')
    marks = input('Marks - ')
    rec = roll+','+name+','+marks+'\n'
    file.write(rec)
file.close()
print('Done')