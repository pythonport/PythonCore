'''
Created on Mar 6, 2019
program to use mysql-connector 2.1.6 to
connect python with mysql
command to install is - pip install mysql-connector
from website - https://pypi.org/project/mysql-connector/
@author: admin
'''
import mysql.connector as mycon

def getDBConnection():
    mydb = mycon.connect(
        host="localhost",
        user="root",
        passwd="bokaro",
        database="jnvbokaro") 
    return mydb

mydb = getDBConnection()
sqlcursor = mydb.cursor()

def insertData(sql,value):
    sqlcursor.execute(sql,value)
    mydb.commit()
    

sql = "insert into employee(ecode,ename,grade,gross)VALUES (%s, %s, %s, %s)"
value = (124,"XYZ", 'A',50000)
#insertData(sql, value)


sql1= "select * from employee"
sqlcursor.execute(sql1)

for a in sqlcursor:
    outstr=''
    for b in a:
        outstr+=str(b)+'\t'
    print(outstr)
    



    