'''
Created on Jan 29, 2025
Code to segregate odd and even number and display 
user has to enter numbers 10 time.
@author: admin
'''
oddlist = []
evenlist = []
for i in range(10):
    num = int(input('Number - '))
    if num%2 == 0 :
        evenlist.append(num)
    else :
        oddlist.append(num)

print('Odds are - ',oddlist)
print('Evens are - ',evenlist)