'''
Created on Mar 4, 2022
Write a program to read roll number and marks of four students and
create a dictionary from it having roll number as keys.
@author: admin
'''

roll = []
marks = []
for a in range(4) :
    r, m = eval(input("[Rollnumber, marks] in form of list - "))
    roll.append(r)
    marks.append(m)

d = {roll[0] : marks[0], roll[1] : marks[1], roll[2] : marks[2], roll[3] : marks[3]}
print(d)

if d[2]>=75 :
    print("roll no 2 scored -",d[2])
else :
    print("roll no 2 scored <75 which is - ",d[2])
    