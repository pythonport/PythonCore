'''
Created on Mar 31, 2021
Write a program in python to illustrate connectivity 
between python and MYSQL and that can display all 
records of a table from database. The table named 
EMPLOYEE (shown below) should be created in MySQL 
before executing the python program. 
@author: admin
'''
import mysql.connector
#creating db object
db = mysql.connector.connect(host="localhost",
                             user="root",
                             password="bokaro",
                             database="tenughat")

#creating cursor object
dbcursor = db.cursor()
query = "select * from employee";
dbcursor.execute(query)
result = dbcursor.fetchall() #fetch all record from database

#printing employee information
for emp in result :
    print('Employee id - ', emp[0])
    print('First Name - ', emp[1])
    print('Last Name - ', emp[2])
    print('Salary - ', emp[3])
    print('Designation - ', emp[4])
    print('-' * 20)
