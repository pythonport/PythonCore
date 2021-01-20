'''
Created on Oct 18, 2019

Reference to -
https://www.w3schools.com/python/python_mysql_select.asp
https://pynative.com/python-mysql-database-connection/
@author: admin
'''
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="bokaro",
  database="jnvbokaro"
)
mycursor = mydb.cursor()


def getAllRecord():
    sql = "SELECT * FROM student"
    # sql = 'Select * from student where fee between {0} and {1} '.format(400,800)
    # sql = 'Select * from student where fee <= {0} '.format(500)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    
    for x in myresult:
        print(x)


def getOneRecord(rollNo):
    # sql = 'Select * from student where sid = %s ' %(rollNo)  #Old Formating
    sql = 'Select * from student where sid = {0} '.format(rollNo)
    mycursor.execute(sql)
    result = mycursor.fetchall()
    if len(result) == 0:
        print("Sorry no match found")
    else :
        print(result)


def insertOneRecord():
    sid = input("enter sid - ")
    sname = input("enter sname - ")
    classes = input("enter class - ")
    fee = input("enter fee - ")
    sql = "insert into student(sid, sname, class, fee) values({0},'{1}',{2},{3})".format(sid, sname, classes, fee)
    
    mycursor.execute(sql)
    mydb.commit()
    print("Data stored successfully.")


def updateFee():
    sid = input("enter sid - ")
    fee = input("enter fee - ")
    sql = "update student set fee={0} where sid={1}".format(fee, sid)
    
    mycursor.execute(sql)
    mydb.commit()
    print("Fee updated successfully.")
    
def deleteStudent():
    sid = input("enter sid - ")
    sql = "delete from student where sid={0}".format(sid)
    
    mycursor.execute(sql)
    mydb.commit()
    print("Record of {0} is deleted successfully.".format(sid))

    
getAllRecord()
'''
roll = input('Enter roll no to get record - ')
getOneRecord(roll)
insertOneRecord()
updateFee()
deleteStudent()
getAllRecord()
'''
