'''
Created on Jan 3, 2026

@author: admin
'''
a = b = c =0
for i in range(1,6):
    a =int(input('First number - '))
    b =int(input('Second number - '))
    if b ==0 :
        print('Zero division not possible')
        continue
    else :
        c = a//b
        print('Quotient - ',c)
print('out and done')