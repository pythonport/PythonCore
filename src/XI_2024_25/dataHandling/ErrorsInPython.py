'''
Created on Dec 20, 2024

@author: admin
'''
a = int(input('Nominator - '))
b = int(input('Denominator - '))
if (b != 0 ) :
    divab = a/b 
    print('division value  of {} and {} is - {}'.format(a,b,divab))
else :
    print('Denominator can not be zero')
    
#----------------    
#run time error when b is zero
a = int(input('Nominator - '))
b = int(input('Denominator - '))
divab = a/b 
print('division value  of {} and {} is - {}'.format(a,b,divab))