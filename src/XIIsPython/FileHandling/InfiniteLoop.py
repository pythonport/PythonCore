'''
Created on Jul 20, 2019

@author: admin
'''
while True :
    sname = input("Student Name - ")
    print(sname)
    flag = input("Do you want to read more[0/1] - ")
    flag = False if flag=='0' else True  
    if flag==False:
        break