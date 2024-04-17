'''
Created on Jan 27, 2022

@author: admin
'''

import mysql.connector

db = mysql.connector.connect(host="localhost",
  user="root",
  password="bokaro",
  database="xiinew")

cur = db.cursor()
rollNo = input("Enter students roll no to get data from db -")
sql = "select * from student where rollno=%s"
roll = (rollNo,)
cur.execute(sql, roll)
result = cur.fetchall()
   
for i in result :
    print(i)
