'''
Created on Aug 10, 2019

@author: admin
'''


def lSearch(ar, item):
    i = 0
    while i < len(ar) and ar[i] != item :
        i += 1
    if i < len(ar):
        return i
    else :
        return False

    
num = int(input("Enter number of element for array [max-50] - "))
print('Enter elements of Learner list \n')
ar = [0] * num
for i in range(num):
    ar[i] = int(input("Enter lement for " + str(i) + " place -"))
print('_'*30)
item = int(input("Enter number to be searched - "))
index = lSearch(ar, num)
if index :
    print('Element found at index :', index, ' and Position - ', (index + 1))
else :
    print('Sorry no match found')