'''
Created on Mar 3, 2026
Program to get Sum, minimum and maximum value of list item
@author: admin
'''
exp = []
for i in range(1,8):
    dayexp = int(input('Expenses -'))
    exp.append(dayexp)

print('Daily expenses - ',exp)
print('Total Expense - ',sum(exp))
print('Minimum Expense - ',min(exp))
print('Maximum Expense - ',max(exp))