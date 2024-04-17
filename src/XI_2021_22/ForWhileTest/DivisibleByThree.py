'''
Created on Apr 6, 2022

@author: admin
'''
for i in range(60, 90, 3) :
    print(i, end=' ')

print('\n-----------------------------')
for i in range(60, 90) :
    if(i % 3 == 0) :
        print(i, end=' ')
        
print('\n-----------------------------')
i = 60
while(i < 90) :
    if(i % 3 == 0) :
        print(i, end=' ')
    i += 1
    
print('\n-----------------------------')
i = 60
while(i < 90) :    
    print(i, end=' ')
    i += 3
