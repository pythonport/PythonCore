'''
Created on Feb 3, 2021

@author: admin
'''
str1 = input("Enter first string - ")
str2 = input("Enter second string - ")

if str1 in str2 :
    str3 = str2[:4] + "Restore"
print("Final String is - ",str3)
