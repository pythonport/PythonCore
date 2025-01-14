'''
Created on Nov 25, 2024

@author: admin
'''
import mysql.connector as connector
myconn = connector.connect(host='localhost', user='root', password = 'dhanbad', database = 'jnvdhanbad')
print('connection done')
mycursor = myconn.cursor()

"""
query = 'select * from pet'
mycursor.execute(query)
data = mycursor.fetchall()
for i in data :
    print(i)



iquery = "insert into pet(name,owner,species) values('{}','{}','{}')".format('sneha','browny','cat')
print(iquery)
mycursor.execute(iquery)
myconn.commit()
"""


iquery = "delete from pet where name = '{}'".format('sneha')
print(iquery)
mycursor.execute(iquery)
myconn.commit()
