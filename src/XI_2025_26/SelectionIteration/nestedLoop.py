'''
Created on Jan 8, 2026

@author: admin
'''
ch = 65
for i in range(6):
    for j in range(i+1):
        print(chr(ch), end = ' ')  #i j
    ch+=1
    print()
    
print('-----------')

for i in range(6):
    ch = 65
    for j in range(i+1):
        print(chr(ch), end = ' ')  #i j
        ch+=1
    print()
    
print('--------')