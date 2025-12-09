'''
Created on Nov 12, 2025

@author: admin
'''
import mysql.connector as jnvconnector
jnvcon = jnvconnector.connect(host ='localhost', user='root', password='dhanbad', database='dhanbaddb')
jnvcursor = jnvcon.cursor()

query = 'select * from supplier'
jnvcursor.execute(query)
row = jnvcursor.fetchone()
print(row)
row = jnvcursor.fetchone()
print(row)
row = jnvcursor.fetchone()
print(row)