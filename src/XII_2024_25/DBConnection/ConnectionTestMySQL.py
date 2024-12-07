'''
Created on Oct 19, 2024
pip install mysql-connector-python
@author: Admin
'''
import mysql.connector
conn = mysql.connector.connect(host='localhost', user='root', password='dhanbad',database='jnvdhanbad')

if conn :
    print('Success to connect')
    
mycursor = conn.cursor()
query = 'select * from items'
mycursor.execute(query)
result = mycursor.fetchall()

for row in result :
    print('item No - ',row[0])
    print('item Name - ',row[1])
    print('item Price - ',row[2])
    print('-----------')