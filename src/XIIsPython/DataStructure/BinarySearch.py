'''
Created on Aug 10, 2019
Binay Search in an array
@author: admin
'''


def bSearch(ar, item):
    beg = 0
    last = len(ar) - 1
    while(beg <= last):
        mid = (beg + last) // 2
        if(item == ar[mid]):
            return mid
        elif(item > ar[mid]):
            beg = mid + 1
        else :
            last = mid - 1
        
    else :
        return False


# main Section   
num = int(input("Enter number of element for array [max-50] - "))
print('Enter elements of Learner list \n')
ar = [0] * num
for i in range(num):
    ar[i] = int(input("Enter lement for " + str(i) + " place -"))
print('_' * 30)
item = int(input("Enter number to be searched - "))
index = bSearch(ar, num)
if index :
    print('Element found at index :', index, ' and Position - ', (index + 1))
else :
    print('Sorry no match found')
