'''
Created on Dec 1, 2025

@author: admin
'''
import mysql.connector as connector
#connect = mysql.connector.connect(host='localhost', user='admin_user', password='hospital_2025', database='HospitalDB')
connect = connector.connect(host='localhost', user='root', password = 'dhanbad', database = 'dhanbaddb')
mycursor = connect.cursor()

Patient_ID = int(input('Patient_ID - '))
Name = input('Name - ')
Age = int(input('Age - '))
Disease = input('Disease - ')

query = "insert into patient_records values({},'{}',{},'{}')".format(Patient_ID, Name,Age, Disease)
print(query)
#mycursor.execute(query)
#connect.commit()

query = 'select * from patient_records'
rows = mycursor.execute(query)
print(rows)
for row in rows :
    print(row)

connect.close()