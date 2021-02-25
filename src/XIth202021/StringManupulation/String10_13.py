'''
Created on Feb 10, 2021

@author: admin
'''
print("Enter word of motto word line by line")

m1 = input("Motto word 1 - ")
m2 = input("Motto word 2 - ")
m3 = input("Motto word 3 - ")
m4 = input("Motto word 4 - ")

motto = ' '.join([m1, m2, m3, m4])
print("Enter foundation date information")
dd = input("Enter DD value - ")
mm = input("Enter MM value - ")
yyyy = input("Enter YYYY value - ")

fdate = '/'.join([dd, mm, yyyy])

print("School motto is - ",motto)
print("School foundation day is - ",fdate)
