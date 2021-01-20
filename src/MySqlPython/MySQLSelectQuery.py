'''
Created on Dec 7, 2020
https://pynative.com/python-mysql-database-connection/
@author: admin
'''
import mysql.connector
from mysql.connector import Error

try :
    dbcon = mysql.connector.connect(host="localhost",
      user="root",
      passwd="bokaro",
      database="xii")    
    mycursor = dbcon.cursor()
    
except Error as e :
    print("Error while connecting to MySQL", e)        


def getEmployeeDetails():
    queryEmp = 'select * from emp'
    mycursor.execute(queryEmp)
    
    result = mycursor.fetchall()
    
    for i in result :
        print("Employee Id - ", i[0])
        print("Employee Name - ", i[1])
        print("Employee Gender - ", i[2])
        print("Employee Grade - ", i[3])
        print("Employee Salary - ", i[4])
        print('====' * 3)

def getEmployeById() :
    pass


def insertEmpoyeeDetails():
    ecode = input('Enter eid - ')
    ename = input('Enter ename - ')
    gender = input('Enter gender - ')
    grade = input('Enter grade - ')
    gross = input('Enter salary - ')
    record = (ecode, ename, gender, grade, gross)
    query = 'insert into emp (ecode, ename, sex, grade, gross) values (%s, %s, %s, %s, %s)'
    
    mycursor.execute(query,record)
    dbcon.commit()
    print("Data inserted successfully")
    
def updateSalary():
    ecode = input('Enter ecode to update Salary - ')
    gross = input('Enter updated Gross Salary - ')
    query = "update emp set gross={0} where ecode={1}".format(gross, ecode)
    
    mycursor.execute(query)
    dbcon.commit()
    print("Data updated successfully")

def deleteEmployee():
    ecode = input('Enter ecode to delete employee record - ')
    query = "delete from emp where ecode={0}".format(ecode)
    
    mycursor.execute(query)
    dbcon.commit()
    print("Record of {0} is deleted successfully.".format(ecode))

#insertEmpoyeeDetails()
#getEmployeeDetails()
#updateSalary()
getEmployeById()
#deleteEmployee()

'''
finally:    
    if (dbcon.is_connected()):
        mycursor.close()
        dbcon.close()
        print("MySQL connection is closed")
'''
