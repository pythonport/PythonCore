'''
Created on Dec 27, 2023
Question from preboard - 1 of session 2023-24
@author: Admin
'''
import mysql.connector
db = mysql.connector.connect(host="localhost",
                             user="root",
                             password="mydb",
                             database="company")
dbcursor = db.cursor()
query = "select * from emp where esalary>40000 and dept = 'manager'"
dbcursor.execute(query)
data = dbcursor.fetchall()
for row in data :
    print(row)
    
#---------------------------
import mysql.connector
db = mysql.connector.connect(host="localhost",
                             user="root",
                             password="mydb",
                             database="shop")
dbcursor = db.cursor()
item_id = input('item_id - ')
itemname = input('itemname - ')
price = input('price - ')
expdate = input('expdate - ')
query = "insert into item(item_id,itemname,price,expdate) values({},'{}',{},'{}')".format(item_id,itemname,price,expdate)
dbcursor.execute(query)
db.commit()
print('OK')