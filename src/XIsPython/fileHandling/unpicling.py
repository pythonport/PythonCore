'''
Created on Apr 03, 2019
import pickle to use load() method to de-serilize the
data from file to python object.
@author: admin
'''
import pickle

class Student :

    def __init__(self, rno=0, name='') :
        self.rollno = rno
        self.name = name
        self.marks1, self.marks2, self.marks3 = 0.0, 0.0, 0.0

    def display(self) :
        print ('Student details are :')
        print ('Roll number :', self.rollno)
        print ('Name :', self.name)
        print ('Marks of 3 subjects :', self.marks1, self.marks2, self.marks3)


stu1 = Student()
f1 = open('student.log', 'rb')
try :
    while True :
        stu1 = pickle.load(f1)
        stu1.display()
except :
    print ("Oops ! Went something wrong")
f1.close()
