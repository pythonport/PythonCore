"""
Write a program to get roll no, name, marks of the students of a class
(get from user) and stores these details in to file called 'marks.dat'
append 2 more students.
"""
fout = open("marks.dat",'a')

for i in range(2) :
    roll = input("Enter roll no - ")
    name = input("Enter name - ")
    marks = input("Enter marks - ")
    rec = roll+','+name+','+marks+'\n'
    fout.write(rec)

print('OK done')
fout.close()
