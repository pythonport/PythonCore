'''
Created on Apr 25, 2019
Code to take input from user and write in file till
users input is true.
@author: admin
'''
fin = open("students.txt", 'a+')  #opended file in append with read
flag = True
while flag :  # while loop infinite
    name = input("Enter student name - ")
    fin.write(name+'\n') #writing data to file with new line character
    uinput = input("Do you want to continue[y/n] - ")
    if uinput != 'y' :
        flag = False
        print("Thank you....")
        break

fin.seek(0) #will take the file pointer at the begning of file
fdata = fin.read() # read data from file with same object fin
print(fdata) #printing data
fin.close()     #closing the file object
