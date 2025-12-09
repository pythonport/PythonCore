'''
Created on Nov 15, 2025
Update database record in python
@author: admin
'''
import mysql.connector as connector
conn = connector.connect(host='localhost',user='root',password ='dhanbad',database='dhanbaddb')
jnvcursor = conn.cursor()

sid = int(input("Sid to update-"))
sname = input("Sname to update-")
query = 'update student set sname="{}" where sid = {}'.format(sname, sid)
print(query)
jnvcursor.execute(query)
conn.commit()  #mandatory to call commit on conection object to save data
print("updated")
conn.close()