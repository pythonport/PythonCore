'''
Created on Jan 03, 2020
Example of Database connection with all CURD Operation
in Python using mysql.connector and mysql
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
sql = "INSERT INTO student (sid, sname, class, fee) VALUES (%s, %s, %s, %s)"

sid = input("enter sid - ")
sname = input("enter sname - ")
classes = input("enter class - ")
fee = input("enter fee - ")
val = (sid, sname, classes, fee)
# val = ("56", "Hari", "8","450")
mycursor.execute(sql, val)
mydb.commit()
print("Data inserted successfully")
