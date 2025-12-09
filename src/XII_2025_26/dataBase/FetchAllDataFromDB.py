'''
before wiring code you need to install below library in site package
pip uninstall mysql-connector
pip install mysql-connector-python
'''

import mysql.connector as jnvconnector
jnvcon = jnvconnector.connect(host ='localhost', user='root', password='dhanbad', database='dhanbaddb')
jnvcursor = jnvcon.cursor()

query = 'select * from student'
jnvcursor.execute(query)
rows = jnvcursor.fetchall()
#rows = jnvcursor.fetchmany()
print(rows)
print('row count - ', jnvcursor.rowcount)
for row in rows :
    print(row)
jnvcon.close()