'''
Created on Dec 30, 2024

@author: admin
'''

lst = [1,2,5,4,8,6,7,9,2,3]

for i in lst :
    if i%2==0 :
        print(i, 'is an even number')
    else :
        print(i, 'is an odd number')

#----------------------   
lst = [1,2,5,4,8,6,7,9,2,3]     
evenlist = []
oddlist = []
for i in lst :
    if i%2==0 :
        evenlist.append(i)
    else :
        oddlist.append(i)

print('Even data is - ',evenlist)
print('Odd data is - ',oddlist)