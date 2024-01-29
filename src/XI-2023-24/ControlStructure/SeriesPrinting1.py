'''
Created on Jan 2, 2024

@author: Admin
'''
for i in range(1,41,3) :
    print(i, end=' ')

print('\n----------')
count = 1
for i in range(1,41,3) :
    val = ''
    if(count%2 == 0) :
        val = '-' + str(i)
    else :
        val = i
    print(val, end=' ')
    count+=1

print('\n----------')
for i in range(1,41,3) :
    if(i%2 == 0) :
        print(-i, end=' ')
    else :
        print(i, end=' ')