'''
Created on Feb 5, 2021

@author: admin
'''

line = input("Enter the line to get details - ")
lowercount = uppercount = digitcount = 0
alphabetcount = speciacount = 0

for a in line :
    if a.islower() :
        lowercount += 1
    elif a.isupper() :
        uppercount += 1
    elif a.isdigit() :
        digitcount += 1
    elif a.isalnum != True and a != ' ' :
        speciacount += 1
    
    if a.isalpha():
        alphabetcount += 1
        
print("Total Lower count - ", lowercount)
print("Total Upper count - ", uppercount)
print("Total Digit count - ", digitcount)
print("Total Alphabet count - ", alphabetcount)
print("Total Special Char count - ", speciacount)
