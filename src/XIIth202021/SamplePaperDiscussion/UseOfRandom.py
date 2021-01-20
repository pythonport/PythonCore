'''
Created on Dec 18, 2020

@author: admin
'''
import random
'''
rnum = random.random() #float number 0<=n<1
print(rnum)
for i in range(5):
    print(random.random())


rnum = random.randint(1,6) #int number between the range l<=n<=u
for i in range(3):
    rnum = random.randint(1,6)
    if rnum==6:
        print('YOU WON....')
        break
else :
    print("YOU Lose....")
    
'''
rnum = random.randrange(10, 20, 2)    
print(rnum)
    
    