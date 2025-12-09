'''
Created on Nov 26, 2024
@author: admin
'''
import mysql.connector as connector
myconn = connector.connect(host='localhost', user='root', password = 'dhanbad', database = 'dhanbaddb')
mycursor = myconn.cursor()

petname = input('Pet Name - ')
owner = input('owner - ')
species = input('species - ')

query  = "insert into pet(name, owner, species) values('{}','{}','{}')".format(petname, owner, species)
mycursor.execute(query)
myconn.commit()
print(petname, "inserted")