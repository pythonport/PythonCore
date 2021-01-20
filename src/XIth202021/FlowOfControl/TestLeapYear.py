'''
Created on Jan 8, 2021

@author: admin
'''
year = int(input("Enter four digit year ="))

if year % 100 == 0:
    if year % 400 == 0:
        print("Leap Century year")   
    else :
        print('Not Century Leap year') 
