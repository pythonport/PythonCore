'''
Created on Jan 7, 2021
A binary file 'STUDENT.DAT' has structure 
(admission_number, Name, Percentage). 
Write a function countrec() in Python that 
would read contents of the file 'STUDENT.DAT' 
and display the details of those students whose 
percentage is above 75. Also display number of 
students scoring above 75%
@author: admin
'''
import pickle


def insertRec() :
    fout = open('STUDENT.DAT', 'ab')
    stulist1 = [111, 'jitendra kumar', 88]
    stulist2 = [123, 'Lallan Lal', 93]
    stulist3 = [512, 'kundan kumar', 71]
    pickle.dump(stulist1, fout)
    pickle.dump(stulist2, fout)
    pickle.dump(stulist3, fout)
    fout.close()


def countrec() :
    fout = open('STUDENT.DAT', 'rb')
    count = 0
    try :
        while True :
            stuList = pickle.load(fout)
            if stuList[2] >= 75 :
                count += 1
                print(stuList)
    except :
        fout.close()
    print("Total ", count, " students stored more then 75% marks")


# insertRec()        
countrec()
