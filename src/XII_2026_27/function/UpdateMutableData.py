'''
Created on Jul 20, 2026

@author: admin
'''
def updateList(lst):
    print('inside function - ',lst)
    lst.append(5)
    print('inside function - ',lst)
    lst.remove(55)
    print('inside function - ',lst)

list1 = [2,3,4,55,66]
print(list1)
updateList(list1)
print(list1)