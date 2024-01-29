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
    return stulist
'''
def showOneStudent(self,rno):
    res = 0
    if self.rollno == rno :
        print("Student rollno : ",self.rollno)
        print("Student name : ",self.name)
        print("Comp Sc : ",self.compsc)
        print("Webapp  : ",self.webapp)
        print("DBMS    : ",self.dbms)
        print("English : ",self.eng)
        print("Hindi   : ",self.hindi)
        self.total = self.compsc+self.webapp+self.dbms+self.eng+self.hindi
        self.percent = (self.total/500)*100
        print("Total   : "+str(self.total))
        print("Percent : "+str(self.percent)+ " % ")
        res = 1
    return res

def showData(self):        
    self.total = self.compsc+self.webapp+self.dbms+self.eng+self.hindi
    self.percent = (self.total/500)*100
    rec = str(self.rollno)+"|"+self.name+"|"+str(self.compsc)+"|"+str(self.webapp)+"|"+str(self.dbms)+"|"+str(self.eng)+"|"+str(self.hindi)+"|"+str(self.total)+"|"+str(self.percent)
    return rec
'''       
def create() :
    ch  = 'y'
    while ch=="y" :
        fout = open("student.csv",'a+')
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
'''
def display() :
    fout = open("student.log",'rb+')
    st = student()
    os.system('cls')
    try :
        print()
        print()
        print()
        header = "ROLLNO"+"|"+"NAME"+"|"+"COMP SC"+"|"+"WEBAPP"+"|"+"DBMS"+"|"+"ENGLISH"+"|"+"HINDI"+"|"+"TOTAL"+"|"+"PERCENT %"
        print(header)
        print("*"*len(header))
        print()
        while True :
            st = pickle.load(fout)
            rec =  st.showData()
            print(rec)
            print("-"*len(header))
    except :
        fout.close()
    ch = input("Do you want to continue y/n :")
    fout.close()
    if ch =="y" :        
        os.system('cls')
        entry.entry_main()

def search() :
    fout = open("student.log",'rb+')
    st = student()
    os.system("cls")
    try :
        print()
        print()
        rno = int(input("Enter Student rollno to search : "))
        print("*"*40)
        print()
        while True :
            st = pickle.load(fout)
            res = st.showOneStudent(rno)
            if res == 1 :
                break
        else :
            print("SORRY NO MATCH FOUND !!!")
        print("*"*40)
    except :
        fout.close()
    ch = input("Do you want to continue y/n :")
    fout.close()
    if ch =="y" :        
        os.system('cls')
        entry.entry_main()
'''