'''
Created on Sep 15, 2026

@author: admin
'''
import csv

def Accept() :
    fout = open('Sales.csv', 'w', newline='')
    jnvwriter = csv.writer(fout)
    #jnvwriter.writerow(['Product_ID','Product_Name','Quantity_Sold','Price_Per_Unit'])
                        
    pid = input('Product_ID - ')
    pname = input('Product_Name - ')
    qty = int(input('Quantity_Sold - '))
    ppu = int(input('Price_Per_Unit - '))
    sales = [pid,pname,qty,ppu]
    jnvwriter.writerow(sales)    
    fout.close()

def CalculateTotalSales() :
    fout = open('Sales.csv', 'r', newline='')
    jnvreader = csv.reader(fout)
    totalSales = 0
    for row in jnvreader :
        rowTotal = int(row[2])* int(row[3])
        totalSales +=rowTotal
    print('Total sales value is - ',totalSales)
    fout.close()

Accept()
CalculateTotalSales()