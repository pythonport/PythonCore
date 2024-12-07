'''
Created on Nov 25, 2024

@author: admin
'''
import mysql.connector as connector
myconn = connector.connect(host='localhost', user='root', password = 'dhanbad', database = 'jnvdhanbad')
print('connection done')
mycursor = myconn.cursor()

query = 'select * from pet'
mycursor.execute(query)
data = mycursor.fetchall()
for i in data :
    print(i)
