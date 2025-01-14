'''
Created on Jan 10, 2025

@author: admin
'''
min = 0 
max = 0
for i in range(5):
    num = int(input('Number - '))
    #min check
    if i == 0 :
        min = num
    elif num < min:
        min = num
    
    #max check    
    if num > max:
        max = num
    
        
print('Maximum - ',max)
print('Minimum - ',min)
