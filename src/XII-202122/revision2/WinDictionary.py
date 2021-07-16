'''
Created on Jul 15, 2021

@author: admin
'''
n = int(input("No of students - "))
winners = {}
for i in range(n):
    name = input('Enter name - ')
    wins = int(input('Enter Winns - '))
    winners[name] = wins
print('Now the dictonary is  - ')
print(winners)

for i in winners.items() :
    print(i)