'''
Created on Jan 7, 2021

@author: admin
'''
class Student(object):  #structure of class
    
    def __init__(self):
        self.stuid = 0
        self.stuname = ""
        self.stumarks = 0.0
    
    def getStudentData(self):
        self.stuid = int(input("Student Id - "))
        self.stuname = input("Student name - ")
        self.stumarks = float(input("Student Marks - "))
    
    def printStudentData(self):
        print("Student ID is - ",self.stuid)
        print("Student name is - ",self.stuname)
        print("Student Marks is - ",self.stumarks)

akash = Student() #object of class student
akash.getStudentData()
akash.printStudentData()
print(akash.stuid)