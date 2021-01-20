'''
Created on Jan 20, 2021
Handling the CSV file
@author: admin
'''
import csv


def enterPhoneDetails():
    file = open("contacts.csv", "a")
    ans = 'y'
    while ans == 'y' :
        name = input("Please enter name - ")
        phone = input("Please enter phone - ")
        file.write(name + "," + phone + "\n")
        print("Record Added Successfully !")
        ans = input("Do you want to add more record [y/n] - ")
    print("Thank you")
    file.close()


def displayPhoneDetails():
    file = open("contacts.csv", "r") 
    csvreader = csv.reader(file)
    print("Name -> Phone Number")
    for row in csvreader :
        print(row[0]," -> ",row[1])
    file.close()

    
# enterPhoneDetails()  
displayPhoneDetails()      
