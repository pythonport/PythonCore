'''
Created on Jul 5, 2021

@author: admin
'''
mobileno = input("Enter 10 digit mobile number - ")

if(mobileno.isdigit() == False) :
    print("Enter digits only")
elif(len(mobileno) != 10):
    print("Mobile Number must be of 10 digit")
else :
    print('Your mobile number is  - {0}'.format(mobileno))
    