'''
Created on Nov 13, 2025

@author: admin
'''
import mysql.connector as connector
conn = connector.connect(host='localhost',user='root',password ='dhanbad',database='dhanbaddb')
jnvcursor = conn.cursor()

sname = input("Enter student name to search - ")
query = 'select * from student where sname = "{}"'.format(sname)
jnvcursor.execute(query)
row = jnvcursor.fetchall()
if len(row)>=1 :
    print(row)
else :
    print('NO record found')
conn.close()