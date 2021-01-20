'''
Created on Mar 18, 2019
import pickle to use dump() method to serilize the
python object into file.
@author: admin
'''
import pickle

class Student : #Student class with readMarks() and display() method

    def __init__(self, rno=0, name='') :
        self.rollno = rno
        self.name = name
        self.marks1, self.marks2, self.marks3 = 0.0, 0.0, 0.0

    def readMarks(self) :
        print('Enter marks of 3 subjects of ', self.name, ' - ')
        self.marks1 = float(input('Subject : 1 - '))
        self.marks2 = float(input('Subject : 2 - '))
        self.marks3 = float(input('Subject : 3 - '))

    def display(self) :
        print('Student details are :')
        print('Roll number :', self.rollno)
        print('Name :', self.name)
        print('Marks of 3 subjects :', self.marks1, self.marks2, self.marks3)


stu1 = Student(1, 'kriti')
stu2 = Student(2, 'sumit')
stu1.readMarks()    #Code to readMarks
stu2.readMarks()    #Code to readMarks

f1 = open('student.log', 'ab')
pickle.dump(stu1, f1)   #calling dump() to serialize stu1 object to f1 file
pickle.dump(stu2, f1)   #calling dump() to serialize stu2 object to f1 file

f1.close()      #fileobjct will get closed
print("We are done")