'''
Created on Jan 12, 2019

Write a program for a phone number of 10 digits and two dashes,
With dashes after the area code and the next three numbers.
for example - 
017-555-1212
Display if the phone number entered is valid format or not and 
display if the phone number is valid or not

@author: Rajesh Kumar Jha
'''

phone = input("Enter valid phone number in [xxx-xxx-xxxx] format -")
flag = True
if len(phone)!=12:
    print("Invalid phone number size!! Please try again.")
    flag = False
    
if (phone[3]!='-' and phone[7]!='-'):
    print("Dashes[-] are not in porper place !! Please try again.")
    flag = False

lst = phone.split('-')
for i in lst :
    print(i)
    if (i.isdigit()==False) :
        print("Alphabets can not part of phone number !! Please try again")
        flag = False
        
    
if flag==True:
    print ("Phone number entered is - ",phone)