'''
Created on Jul 30, 2025

@author: admin
'''
file = open('stumarks.dat','a')
for i in range(2) :
    print(i+1, ': Student Record')
    roll = input('Roll no - ')
    name = input('Name - ')
    marks = input('Marks - ')
    rec = roll+','+name+','+marks+'\n'
    file.write(rec)
file.close()
print('Done')