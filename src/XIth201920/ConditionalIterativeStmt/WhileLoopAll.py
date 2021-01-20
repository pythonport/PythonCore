'''
Created on Nov 13, 2019

@author: admin
'''
a = 5           #initialization
while a>0:      #test-condition
    print("hello - ",a)
    a=a-3 # a-=3    #update

print('loop over')   


num=int(input('Enter number to get table printed - '))   
i=1
while i<11 :
    print(num,'X',i,'=',num*i)
    i+=1