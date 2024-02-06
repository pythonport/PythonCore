import csv
import os
import entry



def getData() :
    stulst = []
    rollno = int(input("Enter roll no : "))
    name = input("Enter name : ")
    comp = float(input("Enter marks of ComputerSc : "))
    eng = float(input("Enter marks of English : "))
    phy = float(input("Enter marks of Physics : "))
    che = float(input("Enter marks of Chemistry : "))
    maths = float(input("Enter marks of Maths : "))
    stulst.append(rollno)
    stulst.append(name)
    stulst.append(comp)
    stulst.append(eng)
    stulst.append(phy)
    stulst.append(che)
    stulst.append(maths)
    return stulst

def showData():   
    os.system("cls")
    fout = open("student.csv",'r+',newline='')
    csvreader = csv.reader(fout) 
    lcount = 0
    for row in csvreader :
        print()
        if lcount== 0:
            for cell in row :
                print(cell, '|',end=' ')
            lcount+=1
        else :
            for cell in row :
                print(cell, '-',end=' ') 
                lcount+=1
     
def create() :
    ch  = 'y'
    while ch=="y" :
        fout = open("student.csv",'a+',newline='')
        csvwriter = csv.writer(fout, delimiter=',')
        os.system('cls')
        print("*"*30)
        csvwriter.writerow(getData())
        print("*"*30)
        print("Student Created Successfully")
        ch = input("Do you want to create more y/n :")
        fout.close()
    if ch !="y" :        
        os.system('cls')
        entry.entry_main()

def search() :
    fout = open("student.csv",'r+',newline='')
    csvreader = csv.reader(fout)
    os.system("cls")
    print()
    print()
    rno = input("Enter Student rollno to search : ")
    print("*"*40)
    print()
    for row in csvreader :
        if row[0] == rno :
            print(row)
            break
    else :
        print("SORRY NO MATCH FOUND !!!")
    print("*"*40)
    ch = input("Do you want to continue y/n :")
    fout.close()
    if ch =="y" :        
        os.system('cls')
        entry.entry_main()
