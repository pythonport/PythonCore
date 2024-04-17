'''
Created on Apr 11, 2022

@author: admin
'''
import random
list = ['Karan','amit','anup','soni','sadhna', 
        'arya','ritik','rahul','sudhanshu','ganga',
        'uday','rprasad','anjali','sagar','reeda']

choosedList = []
for i in range(len(list)) :
    name = random.choice(list)
    if name not in choosedList :
        choosedList.append(name)
    if(len(choosedList)>=3) :
        break
    
print('First luck students are - ',choosedList[0])
print('Second luck students are - ',choosedList[1])
print('Thrid luck students are - ',choosedList[2])
    