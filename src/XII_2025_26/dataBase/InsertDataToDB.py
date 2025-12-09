'''
Created on Nov 13, 2025

@author: admin
'''
import mysql.connector as connector
conn = connector.connect(host='localhost',user='root',password ='dhanbad',database='dhanbaddb')
jnvcursor = conn.cursor()

sid = input("SID - ")
sname = input("Sname - ")
sclass = input("Sclass - ")
address = input("Address - ")
query = 'insert into student(sid, sname, sclass, address) values("{}","{}","{}","{}")'.format(sid,sname,sclass,address)
print(query)
jnvcursor.execute(query)
conn.commit()
print("Inserted")
conn.close()