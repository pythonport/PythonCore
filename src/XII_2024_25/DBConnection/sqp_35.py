'''
Created on Nov 26, 2024
Write the following Python function to perform the specified operation:
AddAndDisplay(): To input details of an item and store it in the table
STATIONERY. The function should then retrieve and display all records
from the STATIONERY table where the Price is greater than 120.
Assume the following for Python-Database connectivity:
Host: localhost, User: root, Password: Pencil
@author: admin
'''
import mysql.connector

def AddAndDisplay() :
    mycon = mysql.connector.connect(host='localhost',user='root',password='Pencil',database='ITEMDB')
    dbcursor = mycon.cursor()
    
    itemNo =input('item no - ')
    itemName=input('item name - ')
    price= input('Price - ')
    qty = input('Quantity - ')
    
    insertquery = 'insert into STATIONERY(itemNo, itemName, price, qty) values ({},{},{},{})'.format(itemNo, itemName, price, qty)
    dbcursor.execute(insertquery)
    dbcursor.commit()
    
    selectquery = 'select * from STATIONERY where price>120'
    dbcursor.execute(selectquery)
    records = dbcursor.fetchall()
    for row in records :
        print(row)