'''
Created on Nov 12, 2025

@author: admin
'''
import mysql.connector as jnvconnector
jnvcon = jnvconnector.connect(host ='localhost', user='root', password='dhanbad', database='dhanbaddb')
jnvcursor = jnvcon.cursor()

city = input("Enter city to data - ")
query = "select * from supplier where city = '{}'".format(city)
print(query)
jnvcursor.execute(query)
rows = jnvcursor.fetchall()

for row in rows :
    print(row)
jnvcon.close()