'''
Created on Nov 3, 2023

@author: Admin
'''
import mysql.connector
conn = mysql.connector.connect(host='localhost', user='root', passwd='dhanbad',database='school')

if conn :
    print('Success to connect')
    
mycursor = conn.cursor()
query = 'select * from customer'
mycursor.execute(query)
result = mycursor.fetchall()

for row in result :
    print(row)